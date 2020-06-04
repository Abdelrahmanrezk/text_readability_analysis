from django import forms
from django.contrib.auth.models import User
from .models import Contact_us



class Contact_us_form(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['first_name', 'mail', 'phonenumber', 'message']