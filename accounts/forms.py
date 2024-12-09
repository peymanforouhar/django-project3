from django import forms

class UserRegisterForm(forms.Form):
    user_name = forms.CharField()
    user_email = forms.EmailField()
    user_password = forms.CharField()

class UserLoginForm(forms.Form):
    user_name = forms.CharField()
    user_password = forms.CharField()