from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from Dashboard.models import Articles, SupportTickets, Reviews
from django.contrib.auth import logout
from taggit.models import Tag
from django.db.models import Q
from jobs.models import *
import ast

# Create your views here.
def signin(request):
        
    if request.user.is_authenticated:
            return redirect('home')     
        
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            try:    
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    login(request, user)
                    if user.is_verified:
                        messages.success(request,"Welcome Back !")
                        return redirect('home')
                    else:
                        messages.error(request,"Email Not Verified !")

                        return redirect('otp_verification')
                else:
                    messages.error(request,"Email or Password is incorrect !")

                    return redirect('loginx')
            except:
                messages.error(request,"Email Not Register")
                return redirect('loginx')
      
    return render(request,'client/login.html')

def candidate_register(request):
    if request.user.is_authenticated:
        return redirect('home')  
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phno')
        whatsapp = request.POST.get('whatsapp')
        dob = request.POST.get('dob')
        
        city = request.POST.get('city')
        state = request.POST.get('state')
        nearest_location= request.POST.get('location')

        qualification= request.POST.get('qualification')
        passing_year= request.POST.get('passing_year')
        additional_qualification= request.POST.get('additional_qualification')
        specialised= request.POST.get('specialised')
        addedSkills = request.POST.getlist('addedSkills')
        
        experience = request.POST.get('experience')
        pic = request.FILES['pic']
        resume= request.FILES['resume']
        addedSkills = request.POST.get('addedSkills')
        exim_yr_experience = request.POST.get('exim_yr_experience')
        exim_mn_experience = request.POST.get('exim_mn_experience')
        current_yr_experience = request.POST.get('current_yr_experience')
        current_mn_experience = request.POST.get('current_mn_experience')
        last_employer =request.POST.get('last_employer')
        
        
        current_industry = request.POST.getlist('current_industry')
        funtional_area = request.POST.get('funtional_area')
        
        current_position =request.POST.get('current_position')
        shipment_expertise =request.POST.get('shipment_expertise')
        operational_area =request.POST.get('operational_area')
        current_salary =request.POST.get('current_salary')

        
        password = request.POST.get('password')
       
        
        
        if User.objects.filter(email=email).exists():
            # pass
            messages.error(request,'Email Already Registered !')
            return render(request,'client/login.html') 
        else:
            # pass
            # if  User.objects.filter(email=email).exists():
            user = User.objects.create(
                email=email,
                username=email,
                phone = phone,
                first_name=first_name,
                last_name = last_name,
                whatsapp=whatsapp,
                dob=dob,
                state=state,
                city=city,
                nearest_station=nearest_location
            )
            # user = User.objects.get(email=email)

        # else:
            
            # user = User.objects.get(email=email)
            candidate = Employee.objects.create(
                user = user,
                qualification=qualification,
                experience=experience,
                passing_year=passing_year,
                additional_qualification=additional_qualification,
                specialised=specialised,
                exim_yr_experience=exim_yr_experience,
                exim_mn_experience=exim_mn_experience,
                current_yr_experience=current_yr_experience,
                current_mn_experience=current_mn_experience,
                last_employer=last_employer,
                current_position=current_position,
                shipment_expertise=shipment_expertise,
                operational_area=operational_area,
                current_salary=current_salary
            )
            
            candidate.profile_pic = pic
            candidate.resume = resume
            
            for k in ast.literal_eval(addedSkills):
                skill = SkillSet.objects.get_or_create(name=k)
                print(skill)
                candidate.skills.add(skill[0].id)
                candidate.save()
            
            for i in current_industry:
                industry = IndustryType.objects.get(id=i)
                print(industry)
                candidate.current_industry.add(industry[0].id)
                
                
            functional_area_ids = [int(id.strip()) for id in funtional_area.split(',')]

            for i in functional_area_ids:
                candidate.funtional_area.add(i)
                       
            candidate.save()
            
            user.set_password(password)
            user.save()
            login(request, user)
            
            if user.is_verified:
                messages.success(request,"Welcome Back !")
                return redirect('home')
            else:
                messages.success(request,'OTP sent on email')
                return redirect('otp_verification')
    industry = IndustryType.objects.all()
    skills = SkillSet.objects.all()
    return render(request,'client/candidate-register.html',{'title':'register','industry':industry,'skills':skills})


# def candidate_register(request):
#     return render(request,'client/candidate-register.html')
def logout_user(request):
    logout(request)
    return redirect('home')




def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = request.user
        if otp == '1234':
            user.is_verified = True
            user.save()
            messages.success(request,"Your Account is Verified !")
            return redirect('home')
        else:
            messages.error(request,"Invalid OTP !")
            return redirect('otp_verification')
    
    return render(request,'client/otp-verification.html',{'title':'otp'})


def reset_password(request):
    return render(request,'client/reset-password.html')


def home(request):
    articles = Articles.objects.order_by('-id')[:3]
    return render(request,'client/index2.html',{"articles":articles})

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number =request.POST.get('phone_number')
        comments = request.POST.get('comments')

        enquiry = SupportTickets.objects.create(first_name=first_name,last_name=last_name, email=email,number=phone_number,comments=comments)
        enquiry.save()
        messages.success(request,'Support Tickets Generated Successfully')
        return redirect('contact')
        
 
    return render(request,'client/contact.html',{'title':'Contact Us'})

def about(request):
    return render(request,'client/about.html',{'title':'About Us'})


def all_articles(request):
    tag = request.GET.get('tag')
    query = request.GET.get('query')
     
    if query:
        # If a query parameter is present, filter articles based on the query
        articles = Articles.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query)
        )
    elif tag:
        # If a tag parameter is present, retrieve the tag and filter articles based on the tag
        articles=[]
        all_articles = Articles.objects.order_by('-id').all()
        for i in all_articles:
            if tag in [j.name for j in i.tags.all()]:
                articles.append(i)

    else:
        # If neither query nor tag parameter is present, retrieve all articles
        articles = Articles.objects.order_by('-id').all()
    tags =Tag.objects.all()
    return render(request,'client/all-articles.html',{'articles':articles,'tags':tags})


def article_details(request,slug):
     article = Articles.objects.get(name=slug)
     
     articles = Articles.objects.order_by('-id')[:3]
     tags =Tag.objects.all()

     return render(request,"client/article-details.html",{'article':article,'articles':articles,'tags':tags})


def wishlist(request):
    wishlist = WishList.objects.filter(user=request.user)
    return render(request,"client/wishlist.html",{'wishlist':wishlist})

def loginpage(request):
    return render(request,"client/loginx.html",{'title':'login'})

def employer_register(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        logo = request.FILES['logo']
        email = request.POST.get('email')
        owner = request.POST.get('owner')
        authorized_person = request.POST.get('authorized_person')
        description = request.POST.get('description')
        no_employess = request.POST.get('no_employess')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        
        linkedin = request.POST.get('linkedin')
        facebook = request.POST.get('facebook')
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        map = request.POST.get('map')
        
        
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Registered !')
            return redirect('employer-register') 
        else:
            user = User.objects.create(username=email,email=email,address=address,city=city,pincode=pincode,state=state,account_type="Employer")
            user.set_password(password)
            user.save()
            recruiter = Recruiter.objects.create(
                user=user,
                company_name=company_name,
                owner=owner,
                employees=no_employess,
                linkedin=linkedin,
                facebook=facebook,
                instagram=instagram,
                twitter=twitter,
                map_location=map,
                authorized_person=authorized_person,
                description=description,
                
            )
            if logo:
                recruiter.company_logo =logo
            recruiter.save()
            login(request, user)
            messages.success(request,"Registration Done !")
            return redirect('otp_verification')
    return render(request,"client/Employer-register.html",{'title':'Recruiter Registration'})


def candidate_profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'client/candidate-home.html')

def employer_profile(request,slug):
    company = Recruiter.objects.get(company_name=slug)
    job_posts = JobPositions.objects.filter(company=company)
    return render(request, 'client/employer-profile.html',{'title':'Profile Settings','company':company,'job_posts':job_posts})


def employer_setting(request):
    return render(request, 'client/employer-profile.html',{'title':'Profile Settings'})

def all_companies(request):
    companies = Recruiter.objects.order_by().all()
    alphabet = sorted(companies, key=lambda x: x.company_name)

    return render(request, 'client/companies.html',{'title':'Profile Settings','companies':alphabet})


from Dashboard.serializers import FunctionalAreaSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def fetchFunctionalArea(request):
    # Get 'ids' from query parameters
    ids = request.GET.get('ids')
    if ids:
        ids_list = ids.split(',')  # Split the string into a list of IDs
        try:
            industries = IndustryType.objects.filter(id__in=ids_list)
            functional_areas = FunctionalArea.objects.filter(industry__in=industries)
            return JsonResponse(FunctionalAreaSerializer(functional_areas, many=True).data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Industries not found'}, status=404)
    return JsonResponse({'error': 'No IDs provided'}, status=400)

import pandas as pd
import numpy as np
def mapIndustry(request):
    df = pd.read_excel('Cleaned_List_of_Industry_Roles.xlsx')
    for index, row in df.iterrows():
        # Get or create the IndustryType
        print(row[1])
        industry_type, created = IndustryType.objects.get_or_create(name=row[1])  # Adjust the column name as necessary
        industry_type.save()
        for i in range(2,len(row)):
            print(row[i],type(row[i]))
            if type(row[i]) != float:
        # Create FunctionalArea for each entry
        # Assuming other columns are to be stored in FunctionalArea model. Adjust 'ColumnName' as necessary.
                functional_area = FunctionalArea.objects.create(
                    industry=industry_type,
                    name=row[i]  # Replace 'FunctionalAreaColumnName' with actual column name
                )
                functional_area.save()
    return JsonResponse('done',safe=False)



def candidate_profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'client/candidate-home.html')

def employer_profile(request,slug):
    company = Recruiter.objects.get(company_name=slug)
    job_posts = JobPositions.objects.filter(company=company)
    return render(request, 'client/employer-profile.html',{'title':'Profile Settings','company':company,'job_posts':job_posts})


def employer_setting(request):
    company = Recruiter.objects.get(user=request.user)
    job_posts = JobPositions.objects.filter(company=company)
    return render(request, 'client/employer-profile.html',{'title':'Profile Settings','company':company,'job_posts':job_posts})


def all_companies(request):
    companies = Recruiter.objects.order_by().all()
    alphabet = sorted(companies, key=lambda x: x.company_name)

    return render(request, 'client/companies.html',{'title':'Profile Settings','companies':alphabet})

def employer_applicant_list(request):
    return render(request, "client/employer-applicant-list.html", {'title': 'Applicant List'})

def employer_notification(request):
    return render(request, "client/employer-notification.html", {'title': 'Notifications'})

def employer_posted_jobs(request):
    return render(request, "client/employer-posted-jobs.html", {'title': 'Posted Jobs'})




from Dashboard.serializers import FunctionalAreaSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def fetchFunctionalArea(request):
    # Get 'ids' from query parameters
    ids = request.GET.get('ids')
    if ids:
        ids_list = ids.split(',')  # Split the string into a list of IDs
        try:
            industries = IndustryType.objects.filter(id__in=ids_list)
            functional_areas = FunctionalArea.objects.filter(industry__in=industries)
            return JsonResponse(FunctionalAreaSerializer(functional_areas, many=True).data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Industries not found'}, status=404)
    return JsonResponse({'error': 'No IDs provided'}, status=400)




def candidate_view(request):
    return render(request, "client/candidate-view.html", {'title': 'Candidate View'})

def candidate_subscription(request):
    return render(request,"client/candidate-subscription.html",{'title':'Subscription'})

def candidate_favourite(request):
    return render(request, "client/candidate-favourite.html", {'title': 'Saved Jobs'})

def candidate_notification(request):
    return render(request, "client/candidate-notification.html", {'title': 'Notifications'})

def candidate_applied(request):
    return render(request, "client/candidate-applied.html", {'title': 'Applied Jobs'})