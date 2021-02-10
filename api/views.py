from django.shortcuts import render
from rest_framework import generics
from api.serializers import membersSerializer, activity_periodsSerializer
from testapp.models import *
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class membersAPIView(generics.ListCreateAPIView):
    queryset=members.objects.all()
    serializer_class=membersSerializer
    pagination_class=PageNumberPagination
# class activity_periodsAPIView(generics.ListCreateAPIView):
#     queryset=activity_periods.objects.all()
#     #serializer_class=BankDetailsSerializer
