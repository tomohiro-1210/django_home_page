from django.urls import path
from .views import *

urlpatterns = [
    path('', blogtop),
    path('<int:pk>/article/', article)    
]
