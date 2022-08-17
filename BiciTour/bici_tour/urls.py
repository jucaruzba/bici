"""bici_tour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name='Principal'),
    path('tours/', views_registros.registros2, name='Tours'),
    path('contact/', views.contact, name='Contacto'),
    path('about/', views.about, name='About'),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('subir',views_registros.archivos,name="Subir"),
    path('consultasSQL',views_registros.consultasSQL,name="sql"),
    path('experiences/',views_registros.experiencias,name="Experiencias"),
    ##Armando
    path('verFormRegistro/<int:id>/',views_registros.verFormRegistro,name="Inscribir"),
    path('Registrando/',views_registros.registrarCliente,name='RegistrarCliente'),
    ##VerListaRegistrados
    path('verListaRegistro/<int:id>/',views_registros.verListaRegistro,name="VerLista"),
    path('Regresando.../',views_registros.regresar,name='Regresar'),

    path('Listando/',views_registros.experiencias,name="VerLista"),
    path('toursR/', views_registros.verToursRealizados, name='ToursR'),
]



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)