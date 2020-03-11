from django.forms import Form
from django.forms import ModelForm
from lavado.models import Articulo

class ArticuloForm(ModelForm):
    class Meta: 
        model = Articulo
        fields = '__all__'
    