from django import forms

    
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
    
    