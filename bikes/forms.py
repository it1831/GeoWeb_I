from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Type, Cyklo


class CykloModelForm(ModelForm):
    def clean_rate(self):
       data = self.cleaned_data['rate']
       if data < 1 or data > 10:
           raise ValidationError('Neplatné hodnocení: musí být v rozsahu 1-10')
       return data

    class Meta:
        model = Cyklo
        fields = ['name', 'type', 'picture', 'description', 'release_date', 'rate']
        labels = {'name': 'označení kola', 'description': 'Stručný popis'}

"""
class CykloForm(forms.Form):
    name = forms.CharField(label='označení kola', help_text='Zadejte název kola', required=True)
    description = forms.CharField(label='Stručný popis', required=False)
    release_date = forms.DateField(label='Datum uvedení', required=True)
    picture = forms.ImageField(label='Obrázek', required=False, help_text='Vkládejte grafické formáty')
    CYKLO_RATE = (
        (1, 1),  
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rate = forms.ChoiceField(choices=CYKLO_RATE, label='Hodnocení')
    types = forms.ModelMultipleChoiceField(queryset = Type.objects.all())
"""