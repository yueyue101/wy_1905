from django.urls import path
from textt import views

urlpatterns = [
    path('index/', views.index),
]