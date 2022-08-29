import email
from django import forms 
from webapp.models import Report
from django_countries.fields import CountryField


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name','last_name','email','passport','appointment_date','appointment_hour']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Report.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo que ingresaste ya está registrado.')
        return email
        
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=40)

class ValidationForm(forms.Form):
    code = forms.CharField(max_length=40)