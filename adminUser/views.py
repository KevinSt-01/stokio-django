from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from productos.models import Producto
from fpdf import FPDF



# Create your views here.
def Adminv_view(request):
    productos = Producto.objects.all()
    return render(request, 'adminUser/adminUser.html', {'productos': productos}) 
    
def registrar_productos_admin(request):
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
        return redirect('registrar_productos_admin')
        
    productos = Producto.objects.all()  
    return render(request,'adminUser/adminUser.html', {'productos': productos})

def editar_productos_admin(request): 
    if request.method == 'POST': 
        nombre_buscar = request.POST.get('nombre_buscar').strip()
        
        try:    
            #Verificar si coinciden. 
            producto = Producto.objects.get(nombre__iexact = nombre_buscar)
        except Producto.DoesNotExist: 
             
                return redirect('adminUser')
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

        return redirect('adminUser')
    
    return redirect('adminUser')

def buscar_productos_admin(request): 
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
            
    return render(request, 'adminUser/adminUser.html',{'productos_encontrados': productos_encontrados,'productos': productos})

def eliminar_productos_admin(request,id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('adminUser') 
    
def generar_pdf(request, id):
    producto = Producto.objects.get(id=id)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)

    pdf.cell(0, 10, "PRODUCTOS", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=11)

    pdf.cell(60, 8, "ID:", 1)
    pdf.cell(0, 8, str(producto.id), 1, ln=True)

    pdf.cell(60, 8, "Nombre:", 1)
    pdf.cell(0, 8, producto.nombre, 1, ln=True)

    pdf.cell(60, 8, "Categoria:", 1)
    pdf.cell(0, 8, producto.categoria, 1, ln=True)

    pdf.cell(60, 8, "Precio:", 1)
    pdf.cell(0, 8, str(producto.precio), 1, ln=True)

    pdf.cell(60, 8, "Stock:", 1)
    pdf.cell(0, 8, str(producto.stock), 1, ln=True)

    pdf.cell(60, 8, "Descripcion:", 1)
    pdf.cell(0, 8, producto.descripcion, 1, ln=True)

    pdf.cell(60, 8, "Fecha ingreso:", 1)
    pdf.cell(0, 8, str(producto.fecha_ingreso), 1, ln=True)

    pdf.cell(60, 8, "Fecha salida:", 1)
    pdf.cell(0, 8, str(producto.fecha_salida), 1, ln=True)

    return HttpResponse(
        bytes(pdf.output(dest="S")),
        content_type="application/pdf"
    )

def reporte_general(request): 
    productos = Producto.objects.all()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    
    pdf.cell(0,10,"PRODUCTOS", ln=True,align="C")
    pdf.ln(5)
    
    pdf.set_font("Arial", size=11)
    
    #Recorrer todos los productos con el FOR para ponerlos en cada celda. 
    
    for producto in productos: 
        pdf.cell(60,8, "ID", 1)
        pdf.cell(0,8, str(producto.id), 1,ln=True)
        
        pdf.cell(60,8, "Nombre", 1)
        pdf.cell(0,8,(producto.nombre), 1,ln=True)
        
        pdf.cell(60,8, "Categoria", 1)
        pdf.cell(0,8,(producto.categoria), 1,ln=True)
        
        pdf.cell(60,8, "Precio", 1)
        pdf.cell(0,8, str(producto.precio), 1,ln=True)
        
        pdf.cell(60,8, "Stock", 1)
        pdf.cell(0,8, str(producto.stock), 1,ln=True)
        
        pdf.cell(60,8, "Descripcion", 1)
        pdf.cell(0,8,(producto.descripcion), 1,ln=True)
        
        pdf.cell(60,8, "Fecha Ingreso", 1)
        pdf.cell(0,8, str(producto.fecha_ingreso), 1,ln=True)
        
        pdf.cell(60,8, "Fecha Salida", 1)
        pdf.cell(0,8, str(producto.fecha_salida), 1,ln=True)
        
        pdf.ln(5)
        
    return HttpResponse(bytes(pdf.output(dest="S")), content_type = "application/pdf")
        
        
        