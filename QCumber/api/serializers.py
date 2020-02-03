"""
This is the serializers for the Course and CourseDetail objects
"""
from rest_framework import serializers

# get all models class
from QCumber.scraper.assets.models import CourseDetail, Course


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
            "url",
            "id",
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
            "url",
            "id",
            "number",
            "subject_name",
            "subject_code",
            "course_details",
        )

# this cannot retrieve the actual val in foreign table but only gets foreign key
