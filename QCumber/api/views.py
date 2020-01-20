# Create your views here.

from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import generics

from QCumber.api.elastic_search.search_indexes import CourseIndex
from QCumber.scraper.assets.models import *


class CourseSerializer(HaystackSerializer):
    class Meta:
        index_classes = [CourseIndex]
        fields = [
            "text", "number", "name"
        ]


class CourseSearchView(HaystackViewSet):
    index_models = [Course]
    serializer_class = CourseSerializer


# Used for read-write endpoints to represent a collection of model instances.


class QCumberListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
