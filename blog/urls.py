from django.urls import path
from .views import *

urlpatterns = [
    path('', blogtop),
    path('test/', test)    
]
