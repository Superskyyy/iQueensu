"""
QCumber views here.
"""
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from QCumber.api.serializers import (
    CourseSerializer,
    CourseDetailSerializer,
    CourseSimpleSerializer,
    GradeDistributionSerializer
)
from QCumber.scraper.assets.models import Course, CourseDetail, GradeDistribution


# https://django-filter.readthedocs.io/en/latest/guide/rest_framework.html

class GradeDistributionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows GradeDistribution to be viewed or edited.
    This viewset should never be queried in production
    as it uses an unoptimized search filter.
    """
    queryset = GradeDistribution.objects.all()
    serializer_class = GradeDistributionSerializer


class CourseDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows coursesDetails to be viewed or edited.
    This viewset should never be queried in production
    as it uses an unoptimized search filter.
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
        "details__learning_hours__learning_hours",
    ]


# https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
# https://stackoverflow.com/questions/24861252/django-rest-framework-foreign-keys-and-filtering
class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides All course related actions
    Search / Filter
    Example: api/v1/qcumber/courses/?search=seminar
    Most fields have spelling error tolerance
    Search + Filter
    Example: api/v1/qcumber/courses/?search=aging&number=816
    """

    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            print("list triggered")

            return CourseSimpleSerializer
        if self.action == "retrieve":
            print("retrieve triggered")
            return CourseSerializer
        return CourseSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "number",
        "subject__name",
        "subject__code",
        "details__units",
        "details__career__career",
        "details__grading_basis__grading",
        "details__course_components__description",
        "details__campus__campus",
        "details__enrollment__enroll_add_consent",
        "details__enrollment__enroll_drop_consent",
    ]

    # permission_classes = [IsAccountAdminOrReadOnly]
    # Todo: Create GIN Index for search performance
    def get_queryset(self):
        """
        Implements search against url parameters
        This enables full text search and trigram similarity search
        README - > Performance issues :
        https://stackoverflow.com/questions/56538419/
        poor-performance-when-trigram-similarity-and-full-text-search-were-combined-with
            __search == Full Text Search
            __trigram_similar == Trigram Match
            None == Exact Match
        """
        courses = Course.objects.all()
        search_term = self.request.query_params.get("search", None)
        if search_term is not None:
            print(f"Search term: {search_term}")

            search_query = SearchQuery(search_term)
            search_vectors = (
                    SearchVector("details__academic_group__academic_group", weight="B")
                    + SearchVector("details__description__description", weight="A")
                    + SearchVector(
                "details__academic_organization__academic_organization", weight="B"
            )
            )

            general_result = (
                Course.objects.annotate(
                    search=search_vectors, rank=SearchRank(search_vectors, search_query)
                )
                    .filter(
                    (
                            Q(search=SearchQuery(search_term))
                            | Q(  # This line enables search on search vectors
                        number=search_term
                    )
                            | Q(subject__name__trigram_similar=search_term)
                            | Q(subject__code=search_term)
                            | Q(details__units__contains=search_term)
                            | Q(details__career__career__trigram_similar=search_term)
                            | Q(
                        details__grading_basis__grading__trigram_similar=search_term
                    )
                            | Q(
                        details__course_components__description__trigram_similar=search_term
                    )
                            | Q(details__campus__campus__trigram_similar=search_term)
                            | Q(details__enrollment__enroll_add_consent=search_term)
                            | Q(details__enrollment__enroll_drop_consent=search_term)
                            | Q(
                        details__learning_hours__learning_hours__contains=search_term
                    )
                    )  # & Q() From here we can add additional filters
                    # Note above line for hours should adapt based on frontend need
                )
                    .order_by("-rank")
            )  # FIXME： 这个排序会导致searchvector结果永远高于trigram 不确定是否有益
            course_name_id_search_result = Course.objects.annotate(
                course_name_id=Concat("subject__code", Value(" "), "number")
            ).filter(course_name_id__search=search_term)
            # print(course_name_id_search_result)
            search_result_courses = general_result | course_name_id_search_result

            return search_result_courses
        return courses
