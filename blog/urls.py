from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('<int:pk>/article/', article),
]
