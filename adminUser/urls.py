from django.urls import path
from . import views

urlpatterns = [
    path('', views.Adminv_view, name='adminUser'),
    path('registrar_admin/', views.registrar_productos_admin, name='registrar_productos_admin'),
    path('editar_admin/', views.editar_productos_admin, name='editar_productos_admin'),
    path('buscar_admin/', views.buscar_productos_admin, name='buscar_productos_admin'),
    path('eliminar_productos_admin/<int:id>/', views.eliminar_productos_admin, name='eliminar_productos_admin'),
    path('reporte-pdf/<int:id>/', views.generar_pdf, name='reporte_pdf'),
    path('reporte_general/', views.reporte_general, name='reporte_general'),
]