from django import forms

class UserForm(forms.Form):

    first_name = forms.CharField(label='First Name', max_length=256)
    
    last_name = forms.CharField(label='Last Name', max_length=256)

    email = forms.EmailField(label='Email', max_length=256)

    age = forms.IntegerField(label='Age', min_value=18)
