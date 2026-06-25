from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # 👈 ESTA ES LA RUTA /
]