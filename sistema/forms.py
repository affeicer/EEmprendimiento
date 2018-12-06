from django import forms
from .models import *

CIUDADES = []
COMUNAS = []
TIPOS = (
	("Procesadores", "Procesadores"),
)
Estados = [
	("Activo", "Activo"),
	("En espera", "En espera"),
]
#
class VentaForm(forms.Form):
	vendedor = forms.ModelChoiceField(label = "Vendedor", queryset = Vendedor.objects.all(), widget = forms.Select(attrs = { "id": "vendedor" }))
	cantidad = forms.IntegerField(label = "Cantidad", widget = forms.NumberInput(attrs = { "id": "cantidad" }))
	comentario = forms.CharField(label = "Comentario", required = False, widget = forms.Textarea(attrs = { "id": "comentario", "placeholder": "Ingrese comentario de la venta" }))
	Tienda = forms.ModelChoiceField(label = "Tienda", queryset = Tienda.objects.all(), widget = forms.Select(attrs = { "id": "tienda" }))
	fechaHora = forms.DateTimeField(label = "Fecha", widget = forms.DateInput(attrs = { "id": "fechaHora" }))

# Formularios
class ProductoForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Ingrese nombre del producto"}))
	Costo_p = forms.IntegerField(label = "Costo Presupuestado", widget = forms.NumberInput(attrs = { "id": "Costo_p" }))
	Costo_real = forms.IntegerField(label = "Costo Real", widget = forms.NumberInput(attrs = { "id": "Costo_real" }))
	Nota = forms.CharField(label = "Notas respecto del producto", widget = forms.TextInput(attrs = { "id": "Nota" , "placeholder": "Ingrese nombre del producto"}))
	Tienda = forms.ModelChoiceField(label = "Tienda", queryset = Tienda.objects.all(), widget = forms.Select(attrs = { "id": "tienda" }))

class VendedorForm(forms.Form):
	run = forms.CharField(label = "RUN", widget = forms.TextInput(attrs = { "id": "run", "placeholder": "12345678-9" }))
	nombres = forms.CharField(label = "Nombres", widget = forms.TextInput(attrs = { "id": "nombres", "placeholder": "Juan Armando" }))
	apPaterno = forms.CharField(label = "Apellido paterno", widget = forms.TextInput(attrs = { "id": "appaterno", "placeholder": "Pérez" }))
	apMaterno = forms.CharField(label = "Apellido materno", widget = forms.TextInput(attrs = { "id": "apmaterno", "placeholder": "Cisternas" }))
	Tienda = forms.ModelChoiceField(label = "Tienda", queryset = Tienda.objects.all(), widget = forms.Select(attrs = { "id": "tienda" }))

class TiendaForm(forms.Form):
	nombre = forms.CharField(label = "Nombre", widget = forms.TextInput(attrs = { "id": "nombre", "placeholder": "Santa Isabel"}))
	ciudad = forms.ChoiceField(label = "Ciudad", choices = CIUDADES, widget = forms.Select(attrs = { "id": "ciudad" }))
	comuna = forms.ChoiceField(label = "Comuna", choices = COMUNAS, widget = forms.Select(attrs = { "id": "comuna" }))
	direccion = forms.CharField(label = "Dirección", widget = forms.TextInput(attrs = { "id": "direccion", "placeholder": "Calle Falsa #123"}))
	telefono = forms.IntegerField(label = "Teléfono", widget = forms.TextInput(attrs = { "id": "telefono", "placeholder": "123456789"}))
	correo = forms.EmailField(label = "Correo electrónico", widget = forms.EmailInput(attrs = { "id": "correo", "placeholder": "direccion@correo.com" }))
	Estado = forms.ChoiceField(label = "Estado Tienda", choices = Estados, widget = forms.Select(attrs ={"id": "estado"}))

class LoginForm(forms.Form):
	username = forms.CharField(label = "Nombre de usuario", widget = forms.TextInput(attrs = { "id": "username", "placeholder": "Ingrese nombre de usuario" }))
	password = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(attrs = { "id": "password", "placeholder": "Ingrese contraseña" }))
