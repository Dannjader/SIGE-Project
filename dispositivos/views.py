from django.contrib.auth import login
from .forms import InputForm, TecnicoForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from dispositivos.models import Dispositivo, Servicio

# # Create your views here.


# def inicio(request):
#     return render(request, 'index.html')
def inicio(request):
    context ={}
    context['form']= InputForm()
    return render(request, "index.html", context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, './registration/login.html', {'form': form})


def dispositivos_list(request):
    dispositivos = Dispositivo.objects.all()
    return render(request, 'dispositivos_list.html', {'dispositivos': dispositivos})


def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios_list.html', {'servicios': servicios})
<<<<<<< HEAD
=======


def reporte_list(request):
    reportes = Reporte.objects.all()
    return render(request, 'reporte_list.html', {'reportes': reportes})

def TecnicoForm(request):
    tecnico= TecnicoForm()
    return render(request, 'tecnico_form.html', {'form':tecnico})
>>>>>>> stayling
