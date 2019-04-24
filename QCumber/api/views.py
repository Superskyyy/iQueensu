from django.http import HttpResponse
# Create your views here.
from QCumber.models import CourseDetail
from QCumber.serializers import CourseDetailSerializer
from rest_framework import generics

'''
def index(request):
    return HttpResponse("Qcumber is Running")

'''
# Used for read-write endpoints to represent a collection of model instances.


class QcumberListCreate(generics.ListCreateAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer

