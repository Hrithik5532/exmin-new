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


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(max_length=20,null=True,blank=True)
    gender = models.CharField(max_length=10, null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=10000, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    newsletter = models.BooleanField(default=False)
    account_type = models.CharField(max_length=20,default="Employee")
    subscription = models.BooleanField(default=False)
    end_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return str(self.username)
    
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    qualification = models.TextField(null=True, blank=True)
    experiance =  models.TextField(null=True, blank=True)
    previous_job_description =  models.TextField(null=True, blank=True)
    skills =  models.ManyToManyField(SkillSet)
    def __str__(self):
        return str(self.user.username)
    

class Recruiter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.TextField(null=True, blank=True)
    owner =  models.TextField(null=True, blank=True)
    employess =  models.TextField(null=True, blank=True)
    wesbsite =  models.URLField(null=True, blank=True)
    company_logo =  models.ImageField(upload_to='company-logo/')
    authorized_person=models.TextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    
    linkedin =  models.URLField(null=True, blank=True)
    facebook =  models.URLField(null=True, blank=True)
    instagram =  models.URLField(null=True, blank=True)
    twitter =  models.URLField(null=True, blank=True)

    map_location = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return str(self.company_name)
    
    
class PaymentDetails(models.Model):
    pass
    
    
class RecruiterPaymentdetails(models.Model):
    payment_detail = models.OneToOneField(PaymentDetails,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status= models.BooleanField(default=False)
    
    