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

        fields = ("enrollment_info")


class CourseDescription(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription

        fields = ("course_description")


class CourseDetailSerializer(serializers.ModelSerializer):
    career = serializers.CharField(source="CareerPossibleValues.career")
    grading = serializers.CharField(source="GradingPossibleValues.grading")
    components = serializers.CharField(source="Components.component_description")
    campus = serializers.CharField(source="CampusPossibleValues.campus")
    academic_group = serializers.CharField(source="AcademicGroupPossibleValues.academic_group")
    academic_organization = serializers.CharField(source="AcademicOrganizationPossibleValues.academic_organization")
    enrollment = serializers.CharField(source="EnrollmentInformation.enrollment_info")
    course_description = serializers.CharField(source="CourseDescription.course_description")

    class Meta:
        model = CourseDetail

        fields = (
            "units", "career", "grading", "components", "campus", "academic_group", "academic_organization",
            "enrollment",
            "course_description")


class CourseSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source="SubjectPossibleValues.subject")
    code = serializers.CharField(source="SubjectPossibleValues.code")
    course_details = CourseDetailSerializer()

    class Meta:
        model = Course

        fields = ("subject", "code", "number", "name", "course_details")

# this cannot retrieve the actual val in foreign table but only gets foreign key
