from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from Dashboard.models import Articles, SupportTickets, Reviews
from django.contrib.auth import logout
from taggit.models import Tag
from django.db.models import Q
from jobs.models import *
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

                    return redirect('login')
            except:
                messages.error(request,"Email Not Register")
                return redirect('login')
      
    return render(request,'client/login.html')

def candidate_register(request):
    if request.user.is_authenticated:
        return redirect('home')  
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Registered !')
            return render(request,'client/login.html') 
        else:
            user = User.objects.create(
                email=email,
                username=email,
                phone = phone,
                first_name=first_name,
                last_name = last_name,
            
            )
            user.set_password(password)
            user.save()
            login(request, user)
            
            if user.is_verified:
                messages.success(request,"Welcome Back !")
                return redirect('home')
            else:
                return redirect('otp_verification')
        
    return render(request,'client/candidate-register.html',{'title':'register'})


# def candidate_register(request):
#     return render(request,'client/candidate-register.html')
def logout_user(request):
    logout(request)
    return redirect('home')

# def otp_verification(request):
#     if request.method == 'POST':
#         user = User.objects.get(email=request.user.email)
#         user.is_verified = True
#         user.save()
#         return redirect('home')
#     return render(request,'client/otp-verification.html')


def otp_verification(request):
    if request.user.is_authenticated:
        return redirect('home')  
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = request.user
        if user.otp == otp:
            user.is_verified = True
            user.save()
            messages.success(request,"Your Account is Verified !")
            return redirect('home')
        else:
            messages.error(request,"Invalid OTP !")
            return redirect('otp_verification')
    
    return render(request,'client/otp_verification.html',{'title':'otp'})

# def resend_otp(request):
#     if request.user.is_authenticated:
#         return redirect('home')  
#     if request.method == 'POST':
#         user = request.user
#         otp = randint(1000,9999)
#         user.otp = otp
#         user.save()
#         send_mail(
#             'OTP for Job Portal',
#             f'Your OTP is {otp}',
#             'jobportal@gmail.com',
#             [user.email],
#             fail_silently=False,
#         )
#         messages.success(request,"OTP Sent Successfully !")
#         return redirect('otp_verification')

def reset_password(request):
    return render(request,'client/reset-password.html')


def home(request):
    articles = Articles.objects.order_by('-id')[:3]
    return render(request,'client/index.html',{"articles":articles})

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
        # logo = request.FILES['logo']
        email = request.POST.get('email')
        owner = request.POST.get('owner')
        authorized_person = request.POST.get('authorized_person')
        description = request.POST.get('description')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
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
                authorized_person=authorized_person,
                description=description,
                
            )
            # if logo:
            #     recruiter.company_logo =logo
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
