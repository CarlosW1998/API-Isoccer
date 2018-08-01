from django.shortcuts import render
from team.serializer import employeeserializer, fansSerializer, recourseSerializer
from team.models import employee, fans, recourse
from rest_framework import status, generics, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

class EmployeesList(generics.ListCreateAPIView) :
    queryset = employee.objects.all()
    serializer_class = employeeserializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = employee.objects.all()
    serializer_class = employeeserializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

class RecourseList(generics.ListCreateAPIView) :
    queryset = recourse.objects.all()
    serializer_class = fansSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
class RecourseDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = recourse.objects.all()
    serializer_class = fansSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

class FansList(generics.ListCreateAPIView) :
    queryset = fans.objects.all()
    serializer_class = fansSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
class FansDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = fans.objects.all()
    serializer_class = fansSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)