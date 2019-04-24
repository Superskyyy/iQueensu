# Create your views here.
from rest_framework import generics

from QCumber.api.serializers import CourseSerializer
from QCumber.scraper.assets.models import Course

'''
def index(request):
    return HttpResponse("Qcumber is Running")

'''


# Used for read-write endpoints to represent a collection of model instances.


class QCumberListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
