from django.urls import path
from Receitas.views import index

urlpatterns = [
    path('', index),
]
