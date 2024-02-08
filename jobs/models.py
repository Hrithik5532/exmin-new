from django.db import models
from Authentication.models import User, Recruiter
from ckeditor.fields import RichTextField 
from Dashboard.models import *
# Create your models here.
class JobPositions(models.Model):
    company = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    industry_type = models.ManyToManyField(IndustryType)
    functional_area = models.ForeignKey(FunctionalArea,models.CASCADE,blank=True, null=True)
    operational_area = models.CharField(max_length=200,blank=True, null=True)
    shipment_expertise = models.CharField(max_length=200,blank=True, null=True)
    position_level = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    job_location = models.CharField(max_length=200,blank=True, null=True)
    international_location = models.CharField(max_length=200,blank=True, null=True)
    minsalary = models.CharField(max_length=200,blank=True, null=True)
    maxsalary = models.CharField(max_length=200,blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    experience=models.CharField(max_length=255,blank=True, null=True)
    max_experience =models.CharField(max_length=255,blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)
    skills_required = models.ManyToManyField(SkillSet)
    created_at = models.DateTimeField(auto_now_add=True)


class WishList(models.Model):
    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE)
    jobposition = models.ForeignKey(JobPositions, related_name='JobPostion', on_delete=models.CASCADE,blank=True, null=True)
    company = models.ForeignKey(Recruiter, related_name='Recruiter', on_delete=models.CASCADE,blank=True, null=True)


class JobApplications(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    job = models.ForeignKey(JobPositions, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
