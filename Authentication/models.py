from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime  # Import the datetime module
import secrets

from ckeditor.fields import RichTextField 
# Create your models here.
class SkillSet(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class IndustryType(models.Model):
    name = models.CharField(unique =True, max_length=200)
    
    def __str__(self) :
        return self.name

class FunctionalArea(models.Model):
    industry = models.ForeignKey(IndustryType,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=200)
    def __str__(self) :
        return self.name
    
    
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=10, null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=10000, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    nearest_station = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    whatsapp = models.CharField(max_length=20,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
    account_type = models.CharField(max_length=20,default="Employee")
    subscription = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.username)
    
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='employee-profile',blank=True, null=True)
    resume = models.ImageField(upload_to='employee-resume',blank=True, null=True)
    
    qualification = models.TextField(null=True, blank=True)
    # experiance =  models.TextField(null=True, blank=True)
    previous_job_description =  models.TextField(null=True, blank=True)
    skills =  models.ManyToManyField(SkillSet)
    passing_year = models.TextField(null=True, blank=True)
    additional_qualification= models.TextField(null=True, blank=True)
    specialised= models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)

    exim_yr_experience= models.CharField(max_length=20,blank=True, null=True)
    exim_mn_experience= models.CharField(max_length=20,blank=True, null=True)
    current_yr_experience= models.CharField(max_length=20,blank=True, null=True)
    current_mn_experience= models.CharField(max_length=20,blank=True, null=True)
    last_employer= models.CharField(max_length=500,blank=True, null=True)
    current_industry = models.ManyToManyField(IndustryType)
    funtional_area = models.ManyToManyField(FunctionalArea)
    shipment_expertise = models.TextField(null=True, blank=True)
    operational_area =models.TextField(null=True, blank=True)
    current_salary = models.TextField(null=True, blank=True)
    
    current_position = models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.user.username)
    

class Recruiter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.TextField(null=True, blank=True)
    owner =  models.TextField(null=True, blank=True)
    employees =  models.TextField(null=True, blank=True)
    website =  models.URLField(null=True, blank=True)
    company_logo =  models.ImageField(upload_to='company-logo/')
    authorized_person=models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    
    linkedin =  models.URLField(null=True, blank=True)
    facebook =  models.URLField(null=True, blank=True)
    instagram =  models.URLField(null=True, blank=True)
    twitter =  models.URLField(null=True, blank=True)

    map_location = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.company_name)
    
    
class PaymentDetails(models.Model):
    pass
    
    
class RecruiterPaymentdetails(models.Model):
    payment_detail = models.OneToOneField(PaymentDetails,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    status= models.BooleanField(default=False)
    
    