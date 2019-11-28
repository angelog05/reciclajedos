from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Para aplicar imagefiel necesitamos instalar Pillows -> pip install Pillow
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True)

    def __str__(self):
        return self.user.username

class Servicio(models.Model):
    nombreservicio = models.CharField(max_length=20)
    valorservicio = models.IntegerField()
    descripcionservicio = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
