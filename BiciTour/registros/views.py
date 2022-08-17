from django.shortcuts import render
from .forms import ComentarioUserForm, FormArchivos, RegistroClienteForm
from .models import Clientes, ComentarioUsuario, Tours, Archivos
from django.contrib import messages
from django.shortcuts import get_object_or_404

def registros(request):
    tours=Tours.objects.all()
    return render(request, "registros/principal.html",{'tours': tours})

def registros2(request):
    tours=Tours.objects.all()
    return render(request, 'registros/tours.html',{'tours': tours})

def registros3(request):
    archivos=Archivos.objects.raw('SELECT id, nombre, email, mensaje, archivo FROM registros_archivos ORDER BY nombre DESC')
    return render(request, 'registros/archivos.html', {'archivos': archivos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioUserForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'registros/archivos.html')
    form = ComentarioUserForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/archivos.html',{'form': form}) 


def archivos(request):
    
    if request.method == 'POST':
        
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombre =request.POST['nombre']
            mensaje =request.POST['mensaje']
            email =request.POST['email']
            archivo =request.FILES['archivo']
            insert = Archivos(nombre=nombre, mensaje=mensaje, email=email, archivo=archivo)
            insert.save()
            archivos = Archivos.objects.all()
            return render(request, 'registros/experiences.html', {'archivos': archivos})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/archivos.html', {'archivo':Archivos})

def consultasSQL(request):
    archivos=Archivos.objects.raw('SELECT id, nombre, email, mensaje, archivo FROM registros_archivos ORDER BY nombre DESC')
    return render (request, 'registros/archivos.html', {'archivos':archivos})

def experiencias(request):
    archivos=Archivos.objects.all()
    return render(request, 'registros/experiences.html',{'archivos': archivos})

##Registro de clientes

def verFormRegistro(request,id):
    tour = Tours.objects.get(id=id)
#  return render(request,"registros/formEditarComentario.html")
#Indicamos el lugar donde se renderizrá el resultado de esta vista
    return render(request,"registros/formRegistrarCliente.html",
    {'tour':tour})


def registrarCliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
                form.save() #inserta
                return render(request,'registros/principal.html') 
    form = RegistroClienteForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/formRegistrarCliente.html',{'form':form}) 

def verListaRegistro(request,id):
    clientes=Clientes.objects.filter(tour_c=id)
    #all recupera todos los objetos del modelo (registros de la tabla alumnos)
    return render(request, "registros/listaRegistrados.html",{'clientes':clientes})

def regresar(request):
    tours=Tours.objects.all()
    return render(request, 'registros/tours.html',{'tours': tours})

def verToursRealizados(request):
    tours=Tours.objects.filter(status="0")
    return render(request, 'registros/toursRealizados.html',{'tours': tours})

    

# def editarAlumno(request,id_a):
#     alumno = get_object_or_404(Alumnos,id_a=id_a)
#     form = AlumnosForm(request.POST, instance=alumno)
#     #referenciamos que el elemento del formulario pertenece al comentario ya existente
#     if form.is_valid(): #Si los datos recibidos son correctos
#             form.save() #inserta
#             alumnos=Alumnos.objects.all()
#             return render(request,"registros/principal.html", {'alumnos':alumnos})
#                     # return render(request,'registros/contacto.html')
#     return render(request,'registros/formEditarAlumno.html',{'alumno': alumno}) 


# def registrar(request):
#     if request.method == 'POST':
#         form = RegistroCursoForm(request.POST)
#         if form.is_valid(): #Si los datos recibidos son correctos
#                 form.save() #inserta
#                 return render(request,'cursos/contacto.html') 
#     form = RegistroCursoForm()
#     #Si algo sale mal se reenvian al formulario los datos ingresados
#     return render(request,'cursos/contacto.html',{'form':form}) 