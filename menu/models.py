from django.db import models

# Create your models here.
#ejemplos despues hay que cambiarlos
class nombre (models.model):
    codigonombre=models.AutoField(primary_key=True) 
    nombreraza=models.CharField(max_length=15)

class Mascota(models.Model):
    codigoChip = models.CharField(max_length=20, primary_key=True)
    nombreMascota = models.CharField(max_length=25,verbose_name='Nombre de la mascota')
    edadMascota = models.IntegerField()
    foto = models.ImageField(upload_to="mascota")
    raza = models.ForeignKey(Raza,on_delete=models.CASCADA)