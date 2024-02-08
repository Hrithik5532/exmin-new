from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'server/index.html')

def user_view(request):
    return render(request,'server/usertable.html')

def menu_view(request):
    return render(request,'server/usertable.html')
    
def candidate_view(request):
    # You would typically fetch candidate data from the database here
    return render(request, 'server/candidate-table.html')

# View for companies
def company_view(request):
    # Fetch company data from the database here
    return render(request, 'server/company-table.html')

# Admin view
def admin_view(request):
    # Fetch admin-related data here
    return render(request, 'server/admin-dashboard.html')

# View for displaying industries
def industry_view(request):
    # Fetch industry data from the database here
    return render(request, 'server/industry_list.html')

# View for adding a new industry
def add_industry(request):
    if request.method == 'POST':
        # Process form data to add a new industry
        pass
    # Render a form for adding a new industry
    return render(request, 'server/add_industry.html')

# View for displaying functional areas
def functional_area_view(request):
    # Fetch functional area data from the database here
    return render(request, 'server/functional-area-list.html')

# View for adding a new functional area
def add_functional_area(request):
    if request.method == 'POST':
        # Process form data to add a new functional area
        pass
    # Render a form for adding a new functional area
    return render(request, 'server/add-functional-area.html')
