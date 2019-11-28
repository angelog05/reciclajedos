from django import forms
from django.contrib.auth.models import User
from .models import PerfilUsuario, Servicio


class   PerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = PerfilUsuario
        fields = ('foto_perfil',)
        # Labels nos cambia el texto del label que corresponde al input
        labels = {
            'foto_perfil': 'Foto de perfil'
        }

class RegistraServicio(forms.ModelForm):
    class Meta():
        model = Servicio
        fields = ('nombre_servicio',
                'valor_servicio',
                'descripcion_servicio',
                'fecha_servicio'
                )
        labels = {
            'nombre_servicio': 'Nombre servicio',
            'valor_servicio': 'Valor servicio',
            'descripcion_servicio': 'Descripción servicio',
            'fecha_servicio': 'Fecha servicio',
            'cliente': 'Cliente'
        }
        exclude = ('cliente',)

class RegistrarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')

    class Meta:
        model = User
        fields = ('username', 
                'email', 
                'password')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo',
            'password': 'Contraseña'
        }
        help_texts = {
            'username': '',
        }
        error_messages = {
            'username': {
                'max_length': 'Maximo 150 caracteres',
                'required': 'Requerido'
            },
            'password': {
                'required': 'Requerido'
            }
        }

    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})