from rest_framework import serializers
from team.models import employee, recourse, fans

class employeeserializer(serializers.ModelSerializer) :
    class meta :
        meta = employee
        fields = (__all__)
class recourseSerializer(serializers.ModelSerializer) :
    class meta :
        meta = recourse
        fields = (__all__)
class fansSerializer(serializers.ModelSerializer) :
    class meta :
        meta = fans
        fields = (__all__)
