from rest_framework import serializers

# get all models class
from QCumber.scraper.assets.models import *


class CareerPossibleValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPossibleValues

        fields = ("career")


class SubjectPossibleValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectPossibleValues

        fields = ("code", "subject")


class CampusPossibleValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusPossibleValues

        fields = ("campus")


class GradingPossibleValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradingPossibleValues

        fields = ("grading")


class AcademicGroupPossibleValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicGroupPossibleValues

        fields = ("academic_group")


class AcademicOrganizationPossibleValues(serializers.ModelSerializer):
    class Meta:
        model = AcademicOrganizationPossibleValues

        fields = ("academic_organization")


class Components(serializers.ModelSerializer):
    class Meta:
        model = Components

        fields = ("component_description")


class EnrollmentInformation(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentInformation

        fields = ("enroll_add_consent", "enroll_drop_consent")


class CourseDescription(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription

        fields = ("course_description")


class CourseDetailSerializer(serializers.ModelSerializer):
    career = serializers.CharField(source="career.career")
    grading = serializers.CharField(source="grading_basis.grading")
    components = serializers.CharField(source="course_components.description")
    campus = serializers.CharField(source="campus.campus")
    academic_group = serializers.CharField(source="academic_group.academic_group")
    academic_organization = serializers.CharField(source="academic_organization.academic_organization")
    enroll_add_consent = serializers.CharField(source="enrollment.enroll_add_consent")
    enroll_drop_consent = serializers.CharField(source="enrollment.enroll_drop_consent")
    course_description = serializers.CharField(source="description.description")

    class Meta:
        model = CourseDetail

        fields = (
            "units",
            "career",
            "grading",
            "components",
            "campus",
            "academic_group",
            "academic_organization",
            "enroll_add_consent",
            "enroll_drop_consent",
            "course_description")


class CourseSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.name")
    subject_code = serializers.CharField(source="subject.code")
    course_details = CourseDetailSerializer(source="details")

    class Meta:
        model = Course

        fields = ("number", "subject_name", "subject_code", "course_details")

# this cannot retrieve the actual val in foreign table but only gets foreign key
