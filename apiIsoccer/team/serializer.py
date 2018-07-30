from rest_framework import serializers
from team.models import employee, recourse, fans

class employeeserializer(serializers.ModelSerializer) :
    class Meta :
        model = employee
        fields = "__all__"
class recourseSerializer(serializers.ModelSerializer) :
    class Meta :
        model = recourse
        fields = "__all__"
class fansSerializer(serializers.ModelSerializer) :
    class Meta :
        model = fans
        fields = "__all__"
