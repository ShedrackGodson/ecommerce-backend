from django.urls import path
from base import views


urlpatterns = [
	path("api/", views.getRoutes, name="routes"),
	path("api/products/", views.getProducts, name="get_products"),
	path("api/products/<int:id>/", views.getProduct, name="get_product"),
]
