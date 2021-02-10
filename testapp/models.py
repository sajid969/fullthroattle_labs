import pytz
from django.db import models
#from timezone_field import TimeZoneField
from datetime import datetime
from django.utils import timezone
# Create your models here.

class members(models.Model):
    id=models.CharField(max_length=9,primary_key=True)
    real_name=models.CharField(max_length=50)
    tz = models.CharField(max_length=50)
    def __str__(self):
        return self.id

class activity_periods(models.Model):
    Members=models.ForeignKey(members, related_name='Activity_Periods',on_delete=models.CASCADE)
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)
