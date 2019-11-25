from .models import form_IS
from django.core.exceptions import ValidationError
from django import forms
from .models import form_IS


class Form(forms.ModelForm):
    pd_country = forms.CharField(max_length=100,required=False)
    pd_Plat_methodology = forms.CharField(max_length=100,required=False)

    class Meta:
        model = form_IS
        fields = ['pd_country','pd_Plat_methodology']
