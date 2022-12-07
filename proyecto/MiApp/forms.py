from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
    
class club_deportivoForm(forms.Form):
    deporte = forms.CharField(max_length = 40)
    nombre = forms.CharField(max_length = 40)
    
class profesorForm(forms.Form):
    deporte = forms.CharField(max_length = 40)
    nombre = forms.CharField(max_length = 40)
    DNI = forms.IntegerField()


class alumnoForm(forms.Form):
    deporte = forms.CharField(max_length = 40)
    nombre = forms.CharField(max_length = 40)
    DNI = forms.IntegerField()
    
    
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]