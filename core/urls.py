from django.urls import path
from .views import home,lista,form_Usuario,Contacto,Cotizar,Trabajos,Login,validarUsuario,administrador,form_mod_vehiculo,form_vehiculo,form_del_vehiculo


urlpatterns = [
    path('', home , name="index"),
    path('listaseries/',lista, name="listaseries"),
    path('form',form_Usuario, name="form_Usuario"),
    path('Contactos',Contacto, name="Contacto"),
    path('Cotizar',Cotizar, name="Cotizar"),
    path('Trabajos',Trabajos, name="Trabajos"),
    path('home', home , name="index"),
    path('login', Login , name="login"),
    path('validarUsuario', validarUsuario),
    path('administrador',administrador, name="administr"),
    path('modificarautos/<id>',form_mod_vehiculo),
    path('form_del_vehiculo/<id>',form_del_vehiculo),
    path('form_vehiculo',form_vehiculo, name="form_vehiculo"),
]