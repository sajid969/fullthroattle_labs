from django.contrib import admin
from testapp.models import *
# Register your models here.


class activity_periodsInline(admin.TabularInline):
    model = activity_periods
    list_display=['start_time','end_time']

class membersAdmin(admin.ModelAdmin):
    list_display=['id','real_name','tz']
    inlines=[activity_periodsInline]

admin.site.register(members,membersAdmin)
