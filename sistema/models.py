from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tienda(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 50)
	ciudad = models.CharField(max_length = 100)
	comuna = models.CharField(max_length = 100)
	telefono = models.IntegerField()
	correo = models.EmailField()
	Estado = models.CharField(max_length = 30)


class Vendedor(models.Model):
	codigo = models.AutoField(primary_key = True)
	usuario = models.OneToOneField(User, unique = True, on_delete = models.DO_NOTHING)
	run = models.CharField(unique = True, max_length = 10)
	nombres = models.CharField(max_length = 30)
	apPaterno = models.CharField(max_length = 20)
	apMaterno = models.CharField(max_length = 20)
	encargado = models.BooleanField(default = True)
	Tienda = models.ForeignKey(Tienda, on_delete = models.DO_NOTHING)

class Producto(models.Model):
	codigo = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 50)
	Costo_p = models.IntegerField()
	Costo_real = models.IntegerField()
	Nota = models.CharField(max_length = 60)
	Tienda = models.ForeignKey(Tienda, on_delete = models.DO_NOTHING)


class Venta(models.Model):
	codigo = models.AutoField(primary_key = True)
	vendedor = models.ForeignKey(Vendedor, on_delete = models.DO_NOTHING)
	Tienda = models.ForeignKey(Tienda, on_delete = models.DO_NOTHING)
	fechaHora = models.DateTimeField(auto_now_add = True)
	producto = models.ForeignKey(Producto, on_delete = models.DO_NOTHING)
	cantidad = models.IntegerField()
	comentario = models.TextField(null = True)
	anulada = models.BooleanField(default = False)
