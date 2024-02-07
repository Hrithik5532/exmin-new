from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Articles),
admin.site.register(SupportTickets)
# admin.site.register(IndustryType)


# class FunctionalAreaAdmin(admin.ModelAdmin):
#     list_filter = ('industry',)

# admin.site.register(FunctionalArea, FunctionalAreaAdmin)