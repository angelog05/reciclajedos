from django.conf.urls import url
from . import views
from django.urls import path
from .api import UserAPI
app_name = 'gestion_usuario'

urlpatterns = [
    path('create_user/', UserAPI.as_view(), name ="api_create_user"),
    path('eliminar_servicio/<int:servicio_id>', views.eliminar_servicio),
    path('editar_servicio/<int:servicio_id>', views.editar_servicio),
    #url('editar_servicio/<int:servicio_id>', views.editar_servicio, name='editar_servicio'),
    url('agregar_servicio/', views.agregar_servicio, name='agregar_servicios'),
    url('listar_servicios/', views.listar_servicios, name='listar_servicios'),
    #url('eliminar_usuario/<int:id_user>',views.eliminar_usuario, name='eliminar_usuario'),
    url('principal/', views.principal, name='principal'),
    url('registrar/', views.registrar, name='registrar'),
    url('login/', views.usuario_login, name='login'),
    url('logout/', views.usuario_logout, name='logout'),
    url('', views.index, name='index'),
]
