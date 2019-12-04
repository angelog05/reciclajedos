from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import RegistrarForm, PerfilUsuarioForm, RegistraServicio
from .models import User, Servicio
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .serializers import ServicioSerializer
from rest_framework import generics

# -----------  SESION ---------------------
# Cierre de sesion
def usuario_logout(request):
    logout(request)
    # return HttpResponseRedirect(reverse('gestion_usuario:principal'))
    return render(request, 'principal.html', {})

# Inicio de sesión
def usuario_login(request):
    # Valida si existe un usuario autenticado
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse, ('gestion_usuario:index'))
    else:
        # Recibe formulario mediante metodo POST
        if request.method == 'POST':
            # Recibimos la informacion del formulario
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Autenticamos el usuario
            user = authenticate(username=username, password=password)
            # Verifica que exista el usuario
            if user:
                # Verifica si el usuario esta activo
                if user.is_active:
                    # Genera un login para autenticar al usuario
                    login(request, user)
                    return HttpResponseRedirect(reverse('gestion_usuario:index'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva.")
            else:
                # Si no existe usuario
                print("username: {} - password: {}".format(username, password))
                return HttpResponse("Datos inválidos")
        else:  # Si llega desde una url en metodo GET (desde el navegador)
            return render(request, 'gestion_usuario/login.html', {})
# -----------  FIN SEISON --------------------

# ----------- RENDERIZACION --------------------
# renderizacion a pagina principal tras iniciar sesion
def index(request):
    if request.user.is_authenticated:
        # Si utilizo esta opcion genera error::
        # TypeError at /
        # quote_from_bytes() expected bytes
        # return HttpResponseRedirect(reverse,('gestion_usuario:index'))
        # Con este return no tiene problemas
        return render(request, 'gestion_usuario/index.html', {})
    else:
        return render(request, 'principal.html', {})

# renderizacion a pagina principal
def principal(request):
    return render(request, 'principal.html', {})

# renderizacion a contacto
def contacto(request):
    return render(request, 'contacto.html', {})

# renderizacion a servicios principales
def servicios_principales(request):
    return render(request, 'servicios.html', {})
# ----------- RENDERIZACION --------------------


# -----------  USUARIO --------------------
# Registrar usuario nuevo
def registrar(request):
    registrado = False
    # Recibe formulario mediante metodo POST
    if request.method == 'POST':
        # Crea formulario de usuario con informacion del request
        user_form = RegistrarForm(data=request.POST)
        # Crea formulario de perfil con informacion del request
        profile_form = PerfilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Guardamos en base de datos
            user = user_form.save()
            # Encripta password con el modelo de django
            user.set_password(user.password)
            # Guarda usuario tras encriptacion
            user.save()
            # Instancia un objeto perfil
            profile = profile_form.save(commit=False)
            # Asigna un usario al perfil
            profile.user = user
            # Valida si en el Array FILES existe el archivo del input foto_perfil
            if 'foto_perfil' in request.FILES:
                # Agrega la imagen al perfil
                profile.foto_perfil = request.FILES['foto_perfil']
            # Guarda en base de datos
            profile.save()
            registrado = True
        else:  # Si alguno de los formularios es invalido
            print(user_form.errors, profile_form.errors)
            return HttpResponse("Datos inválidos")
    else:  # Si no es POST generamos los formularios
        user_form = RegistrarForm()
        profile_form = PerfilUsuarioForm()

    return render(request, 'gestion_usuario/registrar.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registrado': registrado})

# @staff_member_required
#def eliminar_usuario(request, id_user):
#    u = User.objects.get(id=id_user)
#    u.delete()
#    return render(request,'principal.html',{})
# -----------  FIN USUARIO --------------------


# -----------  SERVICIO --------------------
def listar_servicios(request):
    if request.user.is_authenticated:
        # creamos una colección la cual carga TODOS los registos
        servicios = Servicio.objects.all()
        # renderizamos la colección en el template
        return render(request,
            "gestion_usuario/servicio/listar_servicios.html", {'servicios': servicios})
    else:
        return render(request, 'principal.html', {})

def agregar_servicio(request):
    """Agrega nuevo servicio a la BD

    Captura el formulario si es por POST
    valida y guada.

    Excepciones:
     HttpResponse("Los datos del formulario no son validos")
     HttpResponse("Error al guardar")
    
    """
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                serv_form = RegistraServicio(data=request.POST)
                if serv_form.is_valid():
                    serv_form.save()
                    return redirect('servicio/listar_servicios/')
                else:
                    return HttpResponse("Los datos del formulario no son validos")
            else:
                form = RegistraServicio()
                return render(request, 'gestion_usuario/servicio/agregar_servicio.html',
                            {'form': form})
        else:
            return render(request, 'principal.html', {})
    except:
        return HttpResponse("Error al guardar")
    
    #return render(request, 'gestion_usuario/registrar.html',{})

def editar_servicio(request, servicio_id):
    # Verificar si el usuario esta logueado
    if request.user.is_authenticated:
        # Recuperamos el registro de la base de datos por el id
        instancia= Servicio.objects.get(id=servicio_id)
        # creamos un formulario con los datos del objeto
        form=  RegistraServicio(instance=instancia)
        # Compronbamos si se envió el formulario
        if request.method=="POST":
            # Actualizamos el formulario con los datos del objeto
            form= RegistraServicio(request.POST, instance=instancia)
            # Si el formulario es valido....
            if form.is_valid():
                #Guardamos el formulario pero sin confirmar aun
                instancia= form.save(commit=False)
                # grabamos!!!
                instancia.save()
                return redirect('servicio/listar_servicios/')

        return render(request, "gestion_usuario/servicio/editar_servicio.html",{'form':form})
    else:
            return render(request, 'principal.html', {})

def eliminar_servicio(request, servicio_id):
    try:    
        # Verificar si el usuario esta logueado
        if request.user.is_authenticated:
            # Recuperamos el registro de la base de datos por el id
            instancia= Servicio.objects.get(id=servicio_id)
            # Eliminamos el 
            instancia.delete()

            return redirect('/listar_servicios/')
        else:
            return render(request, 'principal.html', {})

    except:
        return redirect('/')   

# No funciona
class ServicioList(generics.ListCreateAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

# -----------  FIN SERVICIO --------------------
