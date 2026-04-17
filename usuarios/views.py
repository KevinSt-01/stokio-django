from django.shortcuts import redirect, render
from .models import Usuarios
from productos.models import Producto


# Create your views here.
def registro_view(request): 
    return render(request, 'usuarios/registro.html')

def registro(request): 
    if request.method == 'POST': 
        username = request.POST['username']
        correo = request.POST['email']
        contraseña = request.POST['password1']
        contraseña2 = request.POST['password2']
        if contraseña != contraseña2: 
            return render(request, 'usuarios/registro.html', {'error': 'Las contraseñas no coinciden.'})
        #Crear el usuario en el panel. 
        usuario = Usuarios.objects.create_user(username=username, correo= correo, password=contraseña)
        usuario.save()
        request.session['usuario_nombre'] = usuario.username
        #Redirijir al Dash.
        return redirect('login_view')

    return render(request, 'usuarios/registro.html')

def login_view(request): 
    productos = Producto.objects.all()
    return render(request,'usuarios/login.html', {'productos': productos})

#Cerrar Sesion
def logout_view(request): 
    request.session.flush() # Borra toda la sesión. 
    return redirect('home')

def registrar_productos(request):
    try:
        if request.method == 'POST': 
            nombre = request.POST.get('username')
            categoria = request.POST.get('categoria')
            precio = request.POST.get('precio')
            cantidad = request.POST.get('cantidad')
            descripcion = request.POST.get('mensaje')
            fecha_ingreso = request.POST.get('fecha_ingreso')
            fecha_salida = request.POST.get('fecha_salida')
            
            fecha_ingreso = fecha_ingreso or None
            fecha_salida = fecha_salida or None
            #Guardar en la BD. 
            Producto.objects.create(nombre=nombre,categoria=categoria,precio=precio,stock=cantidad,descripcion=descripcion,fecha_ingreso = fecha_ingreso, fecha_salida=fecha_salida)
            return redirect('registrar_productos')
    except Exception as e: 
        print("ERROR AL GUARDAR.", e)    
    productos = Producto.objects.all()  
    return render(request,'usuarios/login.html', {'productos': productos})

def editar_productos(request): 
    if request.method == 'POST': 
        nombre_buscar = request.POST.get('nombre_buscar').strip()
        
        try:    
            #Verificar si coinciden. 
            producto = Producto.objects.get(nombre__iexact = nombre_buscar)
        except Producto.DoesNotExist: 
             
                return redirect('login_view')
        #Obtener los valores del form
        if request.POST.get('nombre_new'): 
            #Reemplazarlo con lo que viene del form.
            producto.nombre = request.POST.get('nombre_new')
        if request.POST.get('categoria'): 
            producto.categoria = request.POST.get('categoria')
        if request.POST.get('precio'): 
            producto.precio = request.POST.get('precio')
        if request.POST.get('cantidad'): 
            producto.stock = request.POST.get('cantidad')
        if request.POST.get('descripcion'): 
            producto.descripcion = request.POST.get('descripcion')
        fecha_ingreso = request.POST.get('fecha_ingreso')
        if fecha_ingreso != "":
            producto.fecha_ingreso = fecha_ingreso
            
        fecha_salida = request.POST.get('fecha_salida')
        if fecha_salida != "": 
            producto.fecha_salida = fecha_salida
            
        producto.save()

        return redirect('registrar_productos')
    
    return redirect('login_view')


def buscar_productos(request): 
    productos= Producto.objects.all()
    productos_encontrados = [] 
    
    if request.method == 'POST': 
        nombre = request.POST.get('nombre_buscar','').strip()
        categoria = request.POST.get('categoria','').strip()
        
        #Por Nombre
        if nombre and not categoria: 
            productos_encontrados = Producto.objects.filter(nombre__icontains = nombre)
        elif categoria and not nombre: 
            productos_encontrados = Producto.objects.filter(categoria__icontains = categoria)
        elif nombre and categoria: 
            productos_encontrados = Producto.objects.filter(nombre__icontains = nombre, categoria__icontains = categoria)
            
    return render(request, 'usuarios/login.html',{'productos_encontrados': productos_encontrados,'productos': productos})
            
         
             
            
        

