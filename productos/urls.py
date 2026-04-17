from django.urls import path
from . import views 


urlpatterns = [ 
        path('', views.home, name= 'home'),
        path('login/validacion', views.validacion, name='validacion'),
        path('contacto/', views.contacto, name= 'contacto'),
    ]