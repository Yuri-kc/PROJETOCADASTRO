from django.forms import ModelForm
from app.models import PRODUTO

class PRODUTOForm(ModelForm):
     class Meta:
         model = PRODUTO
         fields = ["NOME", "COR", "MATERIAL", "QUANTIDADE"]