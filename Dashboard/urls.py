from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='dashboard'),
    path('user-view', user_view, name='user-view'),
    path('view-menu', menu_view, name='view-menu'),
    path('candidates/', candidate_view, name='candidates'),
    path('companies/', company_view, name='companies'),
    path('admin/', admin_view, name='admin'),
    # Add more paths as needed
    path('functional-areas/', functional_area_view, name='functional-areas'),
    path('add-functional-area/', add_functional_area, name='add-functional-area'),

]