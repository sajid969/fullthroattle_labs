import pytz
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend_test2.settings')
import django
django.setup()


from testapp.models import members, activity_periods
from faker import Faker
from django.utils import timezone
from random import *
fake=Faker()

def add_members():
    fid=fake.bothify(text='##??#?##?')
    freal_name=fake.name()
    ftz=fake.timezone()
    members_records=members.objects.create(id=fid,real_name=freal_name,tz=ftz)
    members_records.save()
    return members_records

def populate(n):
    for i in range(n):
        fake_members = add_members()
        for j in range(3):
            fstart_time=fake.date_time()
            fend_time=fake.date_time()
            activity_records=activity_periods.objects.get_or_create(Members=fake_members,start_time=fstart_time,end_time=fend_time)
populate(30)
