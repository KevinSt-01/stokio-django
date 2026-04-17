from django.urls import path
from . import views

urlpatterns = [ 
        path('registro/', views.registro_view, name='registro_view'),
        path('registro/guardar', views.registro, name='registro'),
        path('login/', views.login_view, name='login_view'),
        path('logout/', views.logout_view, name='logout'),
        path('registrar/', views.registrar_productos, name='registrar_productos'),
        path('editar/', views.editar_productos, name='editar_productos'),
        path('buscar/', views.buscar_productos, name ='buscar_productos'),
            ]