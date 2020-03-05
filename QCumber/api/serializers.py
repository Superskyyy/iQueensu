"""
This is the serializers for the Course and CourseDetail objects
"""
from django.utils.text import Truncator
from rest_framework import serializers

# get all models class
from QCumber.scraper.assets.models import CourseDetail, Course, GradeDistribution


class CourseDetailSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Course Detail, this can be eliminated if not needed anymore
    """

    career = serializers.CharField(source="career.career")
    grading = serializers.CharField(source="grading_basis.grading")
    components = serializers.CharField(source="course_components.description")
    campus = serializers.CharField(source="campus.campus")
    academic_group = serializers.CharField(source="academic_group.academic_group")
    academic_organization = serializers.CharField(
        source="academic_organization.academic_organization"
    )
    enroll_add_consent = serializers.CharField(source="enrollment.enroll_add_consent")
    enroll_drop_consent = serializers.CharField(source="enrollment.enroll_drop_consent")
    learning_hours = serializers.CharField(source="learning_hours.learning_hours")
    course_description = serializers.CharField(source="description.description")

    class Meta:
        model = CourseDetail

        fields = (
            # "url",
            # "id",
            "units",
            "career",
            "grading",
            "components",
            "campus",
            "academic_group",
            "academic_organization",
            "enroll_add_consent",
            "enroll_drop_consent",
            "learning_hours",
            "course_description",
        )


class CourseDetailSimpleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Course Detail, this can be eliminated if not needed anymore
    """

    career = serializers.CharField(source="career.career")
    grading = serializers.CharField(source="grading_basis.grading")
    # components = serializers.CharField(source="course_components.description")
    campus = serializers.CharField(source="campus.campus")
    academic_group = serializers.CharField(source="academic_group.academic_group")
    # academic_organization = serializers.CharField(
    #    source="academic_organization.academic_organization"
    # )
    # enroll_add_consent = serializers.CharField(source="enrollment.enroll_add_consent")
    # enroll_drop_consent = serializers.CharField(source="enrollment.enroll_drop_consent")
    # learning_hours = serializers.CharField(source="learning_hours.learning_hours")
    # course_description = serializers.CharField(source="description.description")
    course_description_short = serializers.SerializerMethodField(
        method_name="get_course_description_short"
    )

    def get_course_description_short(self, obj):
        """
        Generates a xx words short summary
        """
        description_word_limit = 20
        short = Truncator(obj.description).words(description_word_limit)
        return short

    class Meta:
        model = CourseDetail

        fields = (
            # "url",
            # "id",
            "units",
            "career",
            "grading",
            # "components",
            "campus",
            "academic_group",
            # "academic_organization",
            # "enroll_add_consent",
            # "enroll_drop_consent",
            "course_description_short"
            # "learning_hours",
            # "course_description",
        )


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Course, simply grabs all the objects
    """

    subject_name = serializers.CharField(source="subject.name")
    subject_code = serializers.CharField(source="subject.code")
    course_details = CourseDetailSerializer(source="details")

    class Meta:
        model = Course
        fields = (
            #"url",
            "uuid",
            "number",
            "subject_name",
            "subject_code",
            "course_details",
        )


class CourseSimpleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Course, simply grabs all the objects
    """

    subject_name = serializers.CharField(source="subject.name")
    subject_code = serializers.CharField(source="subject.code")
    course_details = CourseDetailSimpleSerializer(source="details")

    class Meta:
        model = Course
        fields = (
            # "url",
            "uuid",
            "number",
            "subject_name",
            "subject_code",
            "course_details",
        )

class GradeDistributionSerializer(serializers.HyperlinkedModelSerializer):
    """serializer for grade distribution"""
    class Meta:
        model = GradeDistribution
        fields = (
            "gradeDistribution",
        )
