from django.urls import path
from .views import *

urlpatterns = [
    
    path('', job_list, name='job-list'),
    path('/job-details/<int:id>', job_details, name='job-details'),
    path('/job-application/<int:id>', job_application, name='job-application'),
    path('/candidate-details', candidate_view, name='candidate-view'),
    path('/candidate-list', candidate_list, name='candidate-list'),
    path('/job-post', job_post, name='job-post'),

    # Add more paths as needed
]