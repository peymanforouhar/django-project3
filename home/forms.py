from django import forms
from .models import Human


class HumanRegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    family = forms.CharField(max_length=50)
    age = forms.DecimalField()
    address = forms.CharField()
    register_date = forms.DateTimeField()


class HumanEditForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = '__all__'
