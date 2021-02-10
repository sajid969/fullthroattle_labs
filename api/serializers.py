from testapp.models import *
import pytz
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

class activity_periodsSerializer(serializers.ModelSerializer):
    class Meta:
        model=activity_periods
        fields=['start_time', 'end_time']

class membersSerializer(serializers.ModelSerializer):
    tz = TimeZoneSerializerField()
    Activity_Periods=activity_periodsSerializer(read_only=True,many=True)
    class Meta:
        model=members
        fields=['id', 'real_name', 'tz','Activity_Periods']
my_serializer = membersSerializer(data={
    'tz': pytz.timezone('America/Argentina/Buenos_Aires'),
})
