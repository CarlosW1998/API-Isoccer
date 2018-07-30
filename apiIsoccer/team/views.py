from django.shortcuts import render
from team.serializer import employeeserializer, fansSerializer, recourseSerializer
from team.models import employee, fans, recourse
from rest_framework import status, generics, permissions
# Create your views here.

class EmployeesList(generics.ListCreateAPIView) :
    queryset = employee.objects.all()
    serializer_class = employeeserializer
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = employee.objects.all()
    serializer_class = employeeserializer

class RecourseList(generics.ListCreateAPIView) :
    queryset = recourse.objects.all()
    serializer_class = fansSerializer
class RecourseDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = recourse.objects.all()
    serializer_class = fansSerializer

class FansList(generics.ListCreateAPIView) :
    queryset = fans.objects.all()
    serializer_class = fansSerializer
class FansDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = fans.objects.all()
    serializer_class = fansSerializer