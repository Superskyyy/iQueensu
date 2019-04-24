from rest_framework import serializers

# get all models class
from QCumber.models import *

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDetail
        fields = '__all__'

