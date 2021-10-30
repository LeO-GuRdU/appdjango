from django.db import models

class Contactos(models.Model):
    Nombre = models.CharField(max_length=250)
    Apellido = models.CharField(max_length=250)
    Empresa = models.CharField(max_length=250)
    Telefono = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.Nombre + " " + self.Apellido
