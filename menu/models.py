from django.db import models

# Create your models here.
#ejemplos despues hay que cambiarlos
#class nombre (models.Model):
#    codigonombre=models.AutoField(primary_key=True) 
#   nombreraza=models.CharField(max_length=15)

#class Mascota(models.Model):
#    codigoChip = models.CharField(max_length=20, primary_key=True)
#    nombreMascota = models.CharField(max_length=25,verbose_name='Nombre de la mascota')
#    edadMascota = models.IntegerField()
#    foto = models.ImageField(upload_to="mascota")
#    raza = models.ForeignKey(Raza,on_delete=models.CASCADA)
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='pedidos')
    id_direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=50)
    carrito = models.TextField()

class Detalle(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    id_comida = models.ForeignKey('Comida', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Comida(models.Model):
    id_comida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='comida')
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    clave = models.CharField(max_length=100)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=100)

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    codigo_postal = models.CharField(max_length=20)
    id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE)

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', on_delete=models.CASCADE)

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


"""comandos para migrar y actualizar base de datos :
   python manage.py makemigrations
   python manage.py migrate """
