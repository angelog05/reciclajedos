from django.conf.urls import url
from . import views
app_name = 'gestion_usuario'

urlpatterns = [
    url('agregar_servicio', views.agregar_servicio, name='agregar_servicios'),
    url('listar_servicios', views.listar_servicios, name='listar_servicios'),
    url('eliminar_usuario/<int:id_user>',views.eliminar_usuario, name='eliminar_usuario'),
    url('principal/', views.principal, name='principal'),
    url('registrar/', views.registrar, name='registrar'),
    url('login/', views.usuario_login, name='login'),
    url('logout/', views.usuario_logout, name='logout'),
    url('', views.index, name='index'),
]
