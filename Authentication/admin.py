from django.contrib import admin
from Authentication.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(SkillSet)
admin.site.register(Recruiter)
admin.site.register(Employee)
admin.site.register(IndustryType)
admin.site.register(FunctionalArea)