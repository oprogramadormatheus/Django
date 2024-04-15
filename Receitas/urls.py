from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recipes/<int:id>/', views.recipes)
]

