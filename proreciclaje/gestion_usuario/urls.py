from django.conf.urls import url
from . import views
from django.urls import path
from .api import UserAPI
from .views import ServicioList
app_name = 'gestion_usuario'

urlpatterns = [
    # path('servicio_list/', ServicioList.as_view(), name = "servicio_list" ),
    path('create_user/', UserAPI.as_view(), name ="api_create_user"),
    path('eliminar_servicio/<int:servicio_id>', views.eliminar_servicio),
    path('editar_servicio/<int:servicio_id>', views.editar_servicio),
    url('contacto/', views.contacto, name='contacto'),
    url('agregar_servicio/', views.agregar_servicio, name='agregar_servicios'),
    url('listar_servicios/', views.listar_servicios, name='listar_servicios'),
    url('servicios/', views.servicios_principales, name='servicios'),
    url('principal/', views.principal, name='principal'),
    url('registrar/', views.registrar, name='registrar'),
    url('login/', views.usuario_login, name='login'),
    url('logout/', views.usuario_logout, name='logout'),
    url('', views.index, name='index'),
]
