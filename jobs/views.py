from django.shortcuts import render,redirect
# Create your views here.
from Authentication.models import SkillSet,Recruiter,User
from .models import JobPositions,JobApplications
import ast
from django.contrib import messages

from Dashboard.models import IndustryType, FunctionalArea
def job_list(request):
    
    
    
    
    job_list =JobPositions.objects.order_by('-id').all()
    return render(request, 'client/job-list.html',{'job_list':job_list} )


def job_details(request,id):
    job_post = JobPositions.objects.get(id=id)
    return render(request, 'client/job-detail.html',{'job_post':job_post} )



def job_application(request,id):
    if request.user.is_authenticated:
        job_post = JobPositions.objects.get(id=id)
        if request.user.account_type == 'Employee':
            if JobApplications.objects.filter(user=request.user,job=job_post).exists():
                messages.error(request,"Already applied !")
            else:
                job_apply = JobApplications.objects.create(user=request.user,job=job_post)
                job_apply.save()
                messages.success(request,"Application Done")
        return redirect('job-list')
    messages.error(request,'Please Login to apply')
    return redirect('signin')








def candidate_view(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.account_type == 'Employer':
        messages.error(request,"Not allowed")
        return redirect('home')
    return render(request, 'client/candidate-view.html',{'title':'Candidate profile'})


def candidate_list(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.account_type == 'Employer':
        messages.error(request,"Not allowed")
        return redirect('home')
        
    return render(request, 'client/candidate-list.html',{'title':'Candidate List'})


def job_post(request):
    if not request.user.is_authenticated:
        return redirect('')
    if not request.user.account_type == 'Employer':
        messages.error(request,"Not allowed")
        return redirect('home')
        
    if request.method == 'POST':
        job_position = request.POST.get('job_position')
        selectedIndustries = request.POST.get('selectedIndustries')
        functional_area = request.POST.get('functional_area')
        operational_area = request.POST.get('operational_area')
        shipment_expertise = request.POST.get('shipment_expertise')
        position_level = request.POST.get('position_level')
        state = request.POST.get('state')
        city = request.POST.get('city')
        job_location = request.POST.get('job_location')
        international_location = request.POST.get('international_location')
        minsalary = request.POST.get('minsalary')
        maxsalary = request.POST.get('maxsalary')
        benefits = request.POST.get('benefits')
        addedSkills = request.POST.get('addedSkills')
        description = request.POST.get('job_profile')
        experience = request.POST.get('experience')
        end_date = request.POST.get('end_date')
        print(selectedIndustries,'\n',functional_area,'\n',addedSkills)
        
        
        post = JobPositions.objects.create(company=Recruiter.objects.get(user=request.user),
                        operational_area = operational_area,
                        functional_area = FunctionalArea.objects.get(name=functional_area),
                        shipment_expertise=shipment_expertise,
                        position_level=position_level,
                        state=state,city=city,job_location=job_location,
                        international_location=international_location,
                        minsalary=minsalary,maxsalary=maxsalary,benefits=benefits,
                        job_title=job_position,
                        description= description,
                        experience= experience,
                        end_date=end_date
                                           )
        
        for i in ast.literal_eval(selectedIndustries):
            industry = IndustryType.objects.get_or_create(name=i)
            print(industry)
            post.industry_type.add(industry[0].id)
            
    
            
        for k in ast.literal_eval(addedSkills):
            skill = SkillSet.objects.get_or_create(name=k)
            print(skill)
            post.skills_required.add(skill[0].id)
        post.save()
        
            
    industry_type = IndustryType.objects.all()
    functional_area=FunctionalArea.objects.all()
    skill_set = SkillSet.objects.all()
    
    
    return render(request, 'client/job-post.html',{'title':'Post A job','functional_area':functional_area,'industry_type':industry_type,'skill_set':skill_set})