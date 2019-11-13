from django.conf.urls import url
from . import views
app_name = 'gestion_usuario'

urlpatterns = [
    url('', views.index, name='index'),
    url('registar/', views.registrar, name='registar'),
    url('login/', views.usuario_login, name='login'),
    url('logout', views.usuario_logout, name='logout'),
]
