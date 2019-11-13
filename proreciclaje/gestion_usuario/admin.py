from django.contrib import admin
# Para habilitar alternativa 2
# from . import models

# Tuve que importar a PerfilUsuario ya que la linea 11
# no encontraba PersilUsuario y generaba error
from .models import PerfilUsuario

# Register your models here.

# Alternativa 1
admin.site.register(PerfilUsuario)

# Alternativa 2
# admin.site.register(models.PerfilUsuario)
