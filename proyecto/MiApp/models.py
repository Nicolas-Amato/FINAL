from django.db import models

class club_deportivo(models.Model):
    deporte = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    def __str__(self):
        return f' Deporte: {self.deporte} a cargo del Porfesional: {self.nombre}' 

    
    
class profesor(models.Model):
    nombre = models.CharField(max_length = 40)
    deporte = models.CharField(max_length = 40)
    DNI = models.IntegerField()
    def __str__(self):
        return f'nombre: {self.nombre} - deporte: {self.deporte} - DNI: {self.DNI}'


class alumno(models.Model):
    deporte = models.CharField(max_length = 40)
    nombre = models.CharField(max_length = 40)
    DNI = models.IntegerField()
    def __str__(self):
        return f' deporte: {self.deporte} - nombre: {self.nombre} - DNI: {self.DNI}'

    