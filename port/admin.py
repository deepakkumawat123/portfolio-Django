from django.contrib import admin
from.models import *
# Register your models here.

@admin.register(About)
class PortttAdmin(admin.ModelAdmin):
    list_display = ['name','age','dob','mobile','email','city','website','degree','profile','shor_desc','desc','pimg']
# 
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
     list_display = ('tech', )
     search_fields = ('tech',) 

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree','year','university','desc']

admin.site.register(Experience)
admin.site.register(portfolio)
admin.site.register(Service)
