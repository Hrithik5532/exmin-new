from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='dashboard'),
    # Add more paths as needed
]