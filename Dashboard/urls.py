from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='dashboard'),
    
    path('view-menu', menu_view, name='view-menu'),
    path('add-menu', add_menu, name='add-menu'),


    path('candidates', candidate_view, name='candidates'),
    path('companies', company_view, name='companies'),
    path('admin', admin_view, name='admin'),
    # Add more paths as needed
    path('industries/', industry_view, name='industries'),
    path('add_industry/', add_industry, name='add_industry'),

    path('functional-areas', functional_area_view, name='functional-areas'),
    path('add-functional-area', add_functional_area, name='add-functional-area'),

    path('view-position', position_view, name='view-position'),
    path('add-position', add_position, name='add-position'),

    # Paths for qualifications
    path('view-qualification/',view_qualification, name='view-qualification'),
    path('add-qualification/',add_qualification, name='add-qualification'),

    # Paths for states
    path('view-state/',view_state, name='view-state'),
    path('add-state/',add_state, name='add-state'),

    # Paths for cities
    path('view-city/',view_city, name='view-city'),
    path('add-city/',add_city, name='add-city'),

    # Path for vacancies list
    path('vacancies-list/',vacancies_list, name='vacancies-list'),

    # Path for slab list
    path('slab-list/',slab_list, name='slab-list'),

    # Path for changing password
    path('change-password/',change_password, name='change-password'),

]