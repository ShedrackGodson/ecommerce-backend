from django.urls import path
from base import views


urlpatterns = [
	path("api/", views.getRoutes, name="routes"),
	path("api/products/", views.getProducts, name="products"),
]
