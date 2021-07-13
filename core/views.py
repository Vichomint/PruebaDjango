
from django.http import HttpResponse, response
from django.shortcuts import redirect, render
from .models import Vehiculo,Usuario,fotosinfo
from .forms import VehiculoForm,User
from django.http.response import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
    vehiculos = Vehiculo.objects.all()
    foto = fotosinfo.objects.all()
    lista = []
    datos = { 'fotos':foto,'fot':lista}
    for i in datos['fotos']:
        lista.append(i)

    return render(request,'core/index.html',datos)


def lista(request):
    return render(request,'core/listaseries.html')


def form_Usuario(request):
    datos = {
        'form': User
    }
    if request.method == 'POST':
        formulario = User(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form.html', datos)

def Contacto(request):

    return render(request,'core/Contactos.html')

def Trabajos(request):

    return render(request,'core/Trabajos.html')


def Cotizar(request):

    return render(request,'core/Cotizar.html')


def Login(request):

    return render(request,'core/login.html')

def validarUsuario(request):
    try:
        v_email=request.POST.get('email')
        v_password=request.POST.get('password')
        
        usuario=Usuario.objects.get(password=v_password, email=v_email)
        
        request.session['nombre']=usuario.nombre
        return redirect('/home')
        
        
    except Exception as e:
        return HttpResponse(e)
def administrador(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'listaVehiculos':vehiculos
    }
    return render(request,'core/administrador.html',datos)

def cerrarSesion(request):
    del request.session['nombre']
    request.session.modified=True
    return redirect('/')




def form_mod_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }
    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST , instance=vehiculo)
        if formulario.is_valid:
                formulario.save()
                datos['mensaje'] = "Guardados correctamente"
    return render(request,'core/modificarautos.html',datos)




def form_vehiculo(request):
    datos = {
        'form': VehiculoForm
    }
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/agregarvehiculo.html', datos)


def form_del_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect('/home')      