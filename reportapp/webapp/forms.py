from socket import fromshare
from django import forms 
from webapp.models import Report
from django_countries.fields import CountryField

COUNTRIES=[
    ('ecuador','Ecuador'),
    ('argentina','Argentina')
]

class ReportForm(forms.ModelForm):
    country= forms.CharField(label="Cual es tu pais de nacimiento?",widget=forms.Select(choices=COUNTRIES))
    class Meta:
        model = Report
        fields = ['name','last_name','email','passport','appointment_date','appointment_hour']

class ValidationForm(forms.Form):
    code = forms.CharField(max_length=40)