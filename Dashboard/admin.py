from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Articles),
admin.site.register(SupportTickets)
admin.site.register(IndustryType)
admin.site.register(FunctionalArea)