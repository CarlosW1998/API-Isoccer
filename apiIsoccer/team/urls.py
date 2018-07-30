from team import views
from django.conf.urls import url


urlpatterns = [
    url(r'^employee/$', views.EmployeesList.as_view()),
    url(r'^employee/(?P<pk>[0-9]+)$', views.EmployeesDetail.as_view()),

    url(r'^recourse/$', views.RecourseList.as_view()),
    url(r'^recourse/(?P<pk>[0-9]+)$', views.RecourseDetail.as_view()),

    url(r'^fans/$', views.FansList.as_view()),
    url(r'^fans/(?P<pk>[0-9]+)$', views.FansDetail.as_view()),

]