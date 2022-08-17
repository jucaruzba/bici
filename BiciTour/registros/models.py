import email
from django.db import models
from ckeditor.fields import RichTextField

###### Armando

class Tours(models.Model):

    id = models.AutoField(primary_key=True, verbose_name="Identificador") #id

    disponible = models.BooleanField(default=True, verbose_name='STATUS (al desmarcar desaparecerá de "Tours")')#Boleanos
    status = models.BooleanField(default=True, verbose_name='PROXIMOS (al desmarcar se mostrara como un recorrido "Realizado")')#Boleano para realizados

    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    fechaIni=models.DateTimeField(auto_now=False, null=True, verbose_name='Fecha de Inicio')
    ciudad = models.CharField(max_length=200, verbose_name='Ciudad')
    kmreC = models.IntegerField(verbose_name='Km recorridos')
    timeStimed = models.CharField(max_length=100,verbose_name='Tiempo estimado')
    puntoIni = models.CharField(max_length=200, verbose_name='Punto de inicio')
    costo = models.IntegerField(verbose_name='Costo')
    foto = models.ImageField(null=True, verbose_name='Foto', upload_to='fotos')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ['-created']
        
    def __str__(self):
        return self.title

class Clientes(models.Model):

    id_c = models.AutoField(primary_key=True,verbose_name="Clave")
    nombre_c = models.TextField(verbose_name="Nombre")
    apellido_p = models.TextField(verbose_name="Apellido paterno")
    apellido_m = models.TextField(verbose_name="Apellido materno")
    correo_c = models.CharField(max_length=70, verbose_name="Correo")
    telefono_c = models.CharField(max_length=10, default="123", verbose_name="Telefono")
    tour_c = models.ForeignKey(Tours,on_delete=models.CASCADE,verbose_name="Tours")#Llave Foranea
    mensaje_c = models.TextField() #Texto largo
    created =models.DateTimeField(auto_now_add=True,verbose_name="Registrado")
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-created"]
    def __str__(self):
            return self.nombre_c
            #Indica que se mostrára el mensaje como valor en la tabla

# ######################## Armando

class ComentarioUsuario(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.CharField(max_length=100, verbose_name="Correo")
    mensaje = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
        
    def __str__(self):
            return self.mensaje


class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(null=True, max_length=100, verbose_name="Titulo")
    email = models.CharField(null=True, max_length=100, verbose_name="Correo")
    mensaje = models.TextField(null=True, verbose_name="Mensaje")
    archivo = models.FileField(upload_to="archivos", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated  = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Actualizacion")
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ["-created"]
        
    def __str__(self):
            return self.archivo