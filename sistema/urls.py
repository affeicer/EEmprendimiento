from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name = "index"),
	url(r"^cuentas/login$", views.iniciar_sesion, name = "login"),
	url(r"^cuentas/logout$", views.cerrar_sesion, name = "logout"),

	url(r"^gestion$", views.menu_gestion, name = "menu_gestion"),

	# Productos
	url(r"^gestion/productos$", views.gestion_productos, name = "gestion_productos"),
	url(r"^gestion/productos/registrar$", views.registrar_producto, name = "registrar_producto"),
	url(r"^gestion/productos/(?P<pk>[0-9]+)$", views.ver_producto, name = "ver_producto"),
	url(r"^gestion/productos/actualizar/(?P<pk>[0-9]+)$", views.actualizar_producto, name = "actualizar_producto"),
	url(r"^gestion/productos/eliminar/(?P<pk>[0-9]+)$", views.eliminar_producto, name = "eliminar_producto"),

	# Tienda
	url(r"^gestion/Tienda$", views.gestion_Tienda, name = "gestion_Tienda"),
	url(r"^gestion/Tienda/registrar$", views.registrar_Tienda, name = "registrar_Tienda"),
	url(r"^gestion/Tienda/(?P<pk>[0-9]+)$", views.ver_Tienda, name = "ver_Tienda"),
	url(r"^gestion/Tienda/actualizar/(?P<pk>[0-9]+)$", views.actualizar_Tienda, name = "actualizar_Tienda"),
	url(r"^gestion/Tienda/eliminar/(?P<pk>[0-9]+)$", views.eliminar_Tienda, name = "eliminar_Tienda"),
	# Vendedores
	url(r"^gestion/vendedores$", views.gestion_vendedores, name = "gestion_vendedores"),
	url(r"^gestion/vendedores/registrar$", views.registrar_vendedor, name = "registrar_vendedor"),
	url(r"^gestion/vendedores/(?P<pk>[0-9]+)$", views.ver_vendedor, name = "ver_vendedor"),
	url(r"^gestion/vendedores/actualizar/(?P<pk>[0-9]+)$", views.actualizar_vendedor, name = "actualizar_vendedor"),
	url(r"^gestion/vendedores/eliminar/(?P<pk>[0-9]+)$", views.eliminar_vendedor, name = "eliminar_vendedor"),


]
