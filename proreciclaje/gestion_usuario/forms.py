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
        fields = ('nombreservicio',
                'valorservicio',
                'descripcionservicio',
                )
        labels = {
            'nombreservicio': 'Nombre',
            'valorservicio': 'Valor',
            'descripcionservicio': 'Descripción',
        }

    # Define el class="form-control" en los labels del formulario
    def __init__(self, *args, **kwargs):
        super(RegistraServicio, self).__init__(*args, **kwargs)
        self.fields['nombreservicio'].widget.attrs.update({'class': 'form-control'})
        self.fields['valorservicio'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcionservicio'].widget.attrs.update({'class': 'form-control'})

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

    # Define el class="form-control" dentro de los labels del formulario
    def __init__(self, *args, **kwargs):
        super(RegistrarForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
