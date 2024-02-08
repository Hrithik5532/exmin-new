from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('login', signin, name='signin'),
    # path('register', register, name='register'),
    path('OTP-verification', otp_verification, name='otp_verification'),
    path('reset-password', reset_password, name='reset_password'),

    path('contact', contact, name='contact'),
    path('about-us', about, name='about'),
    path('logout', logout_user, name='logout'),
    
    
    
    path('articles',all_articles,name="all_articles"),
    path('article-Details/(?P<slug>[-a-zA-Z0-9_]+)\\Z',article_details,name="article_details"),
    
    
    path('wishlist',wishlist,name="wishlist"),
    path('loginx',loginpage,name="loginx"),

    path('employer-register',employer_register,name="employer-register"),
    path('candidate-register',candidate_register,name="candidate-register"),

    path('candidate-profile', candidate_profile, name='candidate-profile'),
    path('company-profile/(?P<slug>[-a-zA-Z0-9_]+)\\Z', employer_profile, name='company-profile'),
    
    path('employer-setting',employer_setting,name="employer-setting"),
    path('all-companies',all_companies,name="all_companies"),


    path('api-functionalArea/', fetchFunctionalArea),
    path('mapIndustry',mapIndustry),
    path('candidate-subscription', candidate_subscription, name='candidate-subscription'),
    path('candidate-favourite', candidate_favourite, name='candidate-favourite'),
    path('candidate-applied', candidate_applied, name='candidate-applied'),
    path('candidate-notification', candidate_notification, name='candidate-notification'),
    path('candidate-view/', candidate_view, name='candidate_view'),

    
    path('employer-setting',employer_setting,name="employer-setting"),
    path('all-companies',all_companies,name="all_companies"),
    path('employer-notification/', employer_notification, name='employer-notification'),
    path('employer-posted-jobs/', employer_posted_jobs, name='employer-posted-jobs'),
    path('employer-applicant-list/', employer_applicant_list, name='employer-applicant-list'),
]