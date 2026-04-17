from django.shortcuts import render,redirect
from django.contrib import messages
from usuarios.models import Usuarios
from .models import Producto
from django.contrib.auth import authenticate,login
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives

# Create your views here.
#Usuario ADMIN: KevinSt -> 123Kevin 
#Usuario Normal: Stiven Taborda -> 123Stiven



def home(request): 
    return render(request, 'productos/home.html')


def login_view(request): 
    productos = Producto.objects.all()
    return render(request, 'usuarios/login.html', {"productos": productos})


def validacion(request): 
    if request.method == 'POST': 
        nombre = request.POST.get('username')
        contraseña = request.POST.get('password')
        #Validar con la autenticacion de DJANGO.
        user = authenticate(request,username = nombre,password = contraseña)
        
        if user: 
            login(request, user)
            request.session['usuario_nombre'] = user.username
            if user.is_superuser or user.is_staff:
                return redirect("adminUser") 
            return redirect('login_view')
        else: 
            messages.error(request,"Usuario o contraseña incorrectos.")
            return redirect('home')

    return redirect('login_view')
        

"""def validacion(request): 
    if request.method == 'POST':
        nombre = request.POST.get('username')
        contraseña = request.POST.get('password')
        
        try:
            #Validar si son iguales los datos en la BD.
            user = Usuarios.objects.get(nombre = nombre, password = contraseña)
            #Guardar los datos en sesión.
            request.session['usuario_id'] = user.id
            request.session['usuario_nombre'] = user.nombre
            #redirigir a la pagina.
            return redirect('registrar_productos')
        except Usuarios.DoesNotExist:
            return render(request,'productos/home.html',{'error':'Usuario o contraseña incorrectos.'})
    
    return render(request,'usuarios/login.html')"""
    

def contacto(request): 

    if request.method == "POST": 
     
        name = request.POST ['name']
        apellido = request.POST ['ape']
        telefono = request.POST ['tel']
        email = request.POST ['email']
        mensaje = request.POST ['mensaje']
        
        html_content = render_to_string(    
                        'productos/form_contacto.html',  
                        {   
                            'name': name,
                            'apellido': apellido,
                            'telefono': telefono,
                            'email': email,
                            'mensaje': mensaje
                        }  
                    )
        
        try: 
            correo = EmailMultiAlternatives(    
                        subject="Nuevo mensaje desde formulario de contacto",
                        body=f"""Nuevo Mensaje de: 
                            Nombre: {name} {apellido}
                            Teléfono: {telefono}
                            Email: {email}  
                            
                            Mensaje: {mensaje}""",
                            from_email=settings.EMAIL_HOST_USER,
                            to=['stiventaborda10@gmail.com'],
                            reply_to=[email])
            
            correo.attach_alternative(html_content, "text/html")
            correo.send()
            
            messages.success(request,"Se ha enviado tu mensaje correctamente.")
            
        except Exception as e: 
            print("ERROR SMTP", e)
            messages.error(request,"Error al enviar el mensaje.")
        
        return redirect('home')
    




