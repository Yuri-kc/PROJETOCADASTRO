from django.shortcuts import render, redirect
from app.forms import PRODUTOForm
from app.models import PRODUTO
from django.core.paginator import Paginator

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = PRODUTO.objects.filter(NOME__icontains=search)
    else:
        data['db'] = PRODUTO.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = PRODUTOForm()
    return render(request, 'form.html', data)

def create (request):
    form = PRODUTOForm(request.POST or None)
    if form. is_valid():
        form.save()
        return redirect('home')

def view (request, pk):
    data = {}
    data['db'] = PRODUTO.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit (request, pk):
    data = {}
    data['db'] = PRODUTO.objects.get(pk=pk)
    data['form'] = PRODUTOForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = PRODUTO.objects.get(pk=pk)
    form = PRODUTOForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = PRODUTO.objects.get(pk=pk)
    db.delete()
    return redirect ('home')