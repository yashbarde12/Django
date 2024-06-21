from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1)
    salary = forms.DecimalField(min_value=0)