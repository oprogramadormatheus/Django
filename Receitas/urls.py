from django.urls import path
from Receitas.views import index, about, contact

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
]
