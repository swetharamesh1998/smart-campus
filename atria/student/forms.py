from django import forms


class RegistrationForm(forms.Form):
    password = forms.CharField(max_length=8,min_length=8)
    hidden = forms.CharField(hidden=True)