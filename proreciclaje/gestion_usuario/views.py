from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import RegistrarForm, PerfilUsuarioForm

## Cierre de sesion
def usuario_logout(request):
    logout(request)
    ##return HttpResponseRedirect(reverse('gestion_usuario:principal'))
    return render(request, 'principal.html',{})

## renderizacion a pagina inicial
def index(request):
    return render(request, 'gestion_usuario/index.html',{})

## renderizacion a pagina inicial
def principal(request):
    return render(request, 'gestion_usuario/index.html',{})

## Inicio de sesión    
def usuario_login(request):
    ##  Valida si existe un usuario autenticado
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse,('gestion_usuario:index'))
    else:
        # Recibe formulario mediante metodo POST
        if request.method == 'POST':
            ## Recibimos la informacion del formulario
            username = request.POST.get('username')
            password = request.POST.get('password')
            ## Autenticamos el usuario
            user = authenticate(username=username, password=password)
            ## Verifica que exista el usuario
            if user:
                ##Verifica si el usuario esta activo
                if user.is_active:
                    ## Genera un login para autenticar al usuario
                    login(request, user)
                    return HttpResponseRedirect(reverse('gestion_usuario:index'))
                else:
                    return HttpResponse("Tu cuenta esta inactiva.")
            else:
                ## Si no existe usuario
                print("username: {} - password: {}".format(username, password))
                return HttpResponse("Datos inválidos")
        else: ##Si llega desde una url en metodo GET (desde el navegador)
            return render(request, 'gestion_usuario/login.html', {})

## Registrar usuario nuevo
def registrar(request):
    registrado = False
    # Recibe formulario mediante metodo POST
    if request.method == 'POST':
        ## Crea formulario de usuario con informacion del request
        user_form = RegistrarForm(data=request.POST)
        ## Crea formulario de perfil con informacion del request
        profile_form = PerfilUsuarioForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            ## Guardamos en base de datos
            user = user_form.save()
            ## Encripta password con el modelo de django
            user.set_password(user.password)
            ## Guarda usuario tras encriptacion
            user.save()
            ## Instancia un objeto perfil
            profile = profile_form.save(commit=False)
            ## Asigna un usario al perfil
            profile.user = user
            ## Valida si en el Array FILES existe el archivo del input foto_perfil
            if 'foto_perfil' in request.FILES:
                ## Agrega la imagen al perfil
                profile.foto_perfil = request.FILES['foto_perfil']
            ## Guarda en base de datos
            profile.save()
            registrado = True
        else: ## Si alguno de los formularios es invalido
            print(user_form.errors, profile_form.errors)
            return HttpResponse("Datos inválidos")
    else: ## Si no es POST generamos los formularios
        user_form = RegistrarForm()
        profile_form = PerfilUsuarioForm()

    return render(request, 'gestion_usuario/registrar.html', 
                    {'user_form': user_form,
                     'profile_form': profile_form,
                     'registrado': registrado})