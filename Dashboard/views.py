from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'server/index.html')

def add_menu(request):
    return render(request,'server/add-menu.html',{'title':'Add Menu'})

def menu_view(request):
    return render(request, 'server/usertable.html', {'title': 'Menu'})

# View for candidates
def candidate_view(request):
    return render(request, 'server/candidate-table.html', {'title': 'Candidates'})

# View for companies
def company_view(request):
    return render(request, 'server/company-table.html', {'title': 'Companies'})

# Admin view
def admin_view(request):
    return render(request, 'server/admin-dashboard.html', {'title': 'Admin Dashboard'})

# View for displaying industries
def industry_view(request):
    return render(request, 'server/industry_list.html', {'title': 'Industries'})

# View for adding a new industry
def add_industry(request):
    if request.method == 'POST':
        pass
    return render(request, 'server/add_industry.html', {'title': 'Add Industry'})

# View for displaying functional areas
def functional_area_view(request):
    return render(request, 'server/functional-area-list.html', {'title': 'Functional Areas'})

# View for adding a new functional area
def add_functional_area(request):
    if request.method == 'POST':
        pass
    return render(request, 'server/add-functional-area.html', {'title': 'Add Functional Area'})

# View for positions
def position_view(request):
    return render(request, 'server/position-view.html', {'title': 'View Positions'})

def add_position(request):
    return render(request, 'server/add-position.html', {'title': 'Add Position'})

# Views for qualifications
def view_qualification(request):
    return render(request, 'server/view_qualification.html', {'title': 'View Qualifications'})

def add_qualification(request):
    return render(request, 'server/add_qualification.html', {'title': 'Add Qualification'})

# Views for states
def view_state(request):
    return render(request, 'server/view_state.html', {'title': 'View States'})

def add_state(request):
    return render(request, 'server/add_state.html', {'title': 'Add State'})

# Views for cities
def view_city(request):
    return render(request, 'server/view_city.html', {'title': 'View Cities'})

def add_city(request):
    return render(request, 'server/add_city.html', {'title': 'Add City'})

# View for listing vacancies
def vacancies_list(request):
    return render(request, 'server/vacancies_list.html', {'title': 'Vacancies List'})

# View for listing slabs
def slab_list(request):
    return render(request, 'server/slab_list.html', {'title': 'Slab List'})

# View for changing password
def change_password(request):
    return render(request, 'server/change_password.html', {'title': 'Change Password'})
