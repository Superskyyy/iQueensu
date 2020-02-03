"""
QCumber views here.
"""

from rest_framework import filters
from rest_framework import viewsets

from QCumber.api.serializers import *


class CourseDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "units",
        "career",
        "grading",
        "components",
        "campus",
        "academic_group",
        "academic_organization",
        "enroll_add_consent",
        "enroll_drop_consent",
        "course_description",
    ]


# https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
# https://stackoverflow.com/questions/24861252/django-rest-framework-foreign-keys-and-filtering
class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = [
        "subject__code",
        "subject__name",
        "=number",
        "@name",
        "^details__units",
        "@details__career__career",
        "@details__grading_basis__grading",
        "@details__course_components__description",
        "@details__campus__campus",
        "@details__academic_group__academic_group",
        "@details__academic_organization__academic_organization",
        "@details__enrollment__enroll_add_consent",
        "@details__enrollment__enroll_drop_consent",
        "@details__learning_hours__learning_hours",
        "@details__description__description",
    ]
    # change to @ for name
