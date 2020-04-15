"""
This is the models for QCumber courses,
Only Course and CourseDetails are serialized.
"""
import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


# Create your models here.


# These table are claimed for better performance
class CareerPossibleValues(models.Model):
    """
    Career table for reusable entries
    """

    career = models.CharField(max_length=128)

    def __str__(self):
        return self.career or 'null'


class SubjectPossibleValues(models.Model):
    """
    Subject table for reusable entries, this table contains the subject code + name
    """

    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return (self.code + " - " + self.name) or 'null'


class CampusPossibleValues(models.Model):
    """
    Campus, e.g. Main
    """

    campus = models.CharField(max_length=128)

    def __str__(self):
        return self.campus or 'null'


class GradingPossibleValues(models.Model):
    """
    Grading. E.g. "grading": "Pass/Fail",
    """

    grading = models.CharField(max_length=128)

    def __str__(self):
        return self.grading or 'null'


class AcademicGroupPossibleValues(models.Model):
    """
    E.g. "academic_group": "School of Graduate Studies",
    """

    academic_group = models.CharField(max_length=128)

    def __str__(self):
        return self.academic_group or 'null'


class AcademicOrganizationPossibleValues(models.Model):
    """
    E.g. "academic_organization": "REH (not department specific)",
    """

    academic_organization = models.CharField(max_length=128)

    def __str__(self):
        return self.academic_organization or 'null'


class Components(models.Model):
    """
    E.g. "components": "Seminar",
    """

    description = models.TextField(null=True)

    def __str__(self):
        return self.description or 'null'


class EnrollmentInformation(models.Model):
    """
    E.g.
    "enroll_add_consent": "Department Consent Required",
    "enroll_drop_consent": "Department Consent Required",
    """

    enroll_add_consent = models.TextField(null=True)
    enroll_drop_consent = models.TextField(null=True)

    def __str__(self):
        return (self.enroll_add_consent + "-" + self.enroll_drop_consent) or 'null'


class LearningHours(models.Model):
    """
    E.g.
    "learning_hours": "144 (48Lb;96P)",
    """

    learning_hours = models.TextField(null=True)

    def __str__(self):
        return self.learning_hours or 'null'


class CourseDescription(models.Model):
    """
    Simply course description as a Text.
    """

    description = models.TextField(null=True)

    def __str__(self):
        return self.description + "-" or 'null'

class GradeDistribution(models.Model):
    """All grade distribution including following fields"""
    name = models.CharField(max_length=200)
    data = JSONField()
    uuid_text = models.TextField(null=True)
    def __str__(self):
        # return self.name + '\t' + self.uuid_text
        return self.name

# actual representative tables
class CourseDetail(models.Model):
    """
    All CourseDetails including following fields
    """

    career = models.ForeignKey(
        CareerPossibleValues, on_delete=models.SET_NULL, blank=True, null=True
    )
    units = models.TextField(null=True)
    grading_basis = models.ForeignKey(
        GradingPossibleValues, on_delete=models.SET_NULL, blank=True, null=True
    )
    course_components = models.ForeignKey(
        Components, on_delete=models.SET_NULL, blank=True, null=True
    )
    campus = models.ForeignKey(
        CampusPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="campus_names",
    )
    academic_group = models.ForeignKey(
        AcademicGroupPossibleValues, on_delete=models.SET_NULL, blank=True, null=True
    )
    academic_organization = models.ForeignKey(
        AcademicOrganizationPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    enrollment = models.ForeignKey(
        EnrollmentInformation, on_delete=models.SET_NULL, blank=True, null=True
    )
    learning_hours = models.ForeignKey(
        LearningHours, on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.ForeignKey(
        CourseDescription, on_delete=models.SET_NULL, blank=True, null=True
    )


    def __str__(self):
        return (
                "Career \t"
                + self.career.__str__()
                + "\n"
                + "Units \t"
                + self.units.__str__()
                + "\n"
                + "Grading Basis \t"
                + self.grading_basis.__str__()
                + "\n"
                + "Course Components \t"
                + self.course_components.__str__()
                + "\n"
                + "Campus \t"
                + self.campus.__str__()
                + "\n"
                + "Academic Group \t"
                + self.academic_group.__str__()
                + "\n"
                + "Academic Organization \t"
                + self.academic_organization.__str__()
                + "\n"
                + "Enrollment Information \t"
                + self.enrollment.__str__()
                + "\n"
                + "Learning Hours \t"
                + self.learning_hours.__str__()
                + "\n"
                + "Description \t"
                + self.description.__str__()
        )


class Course(models.Model):
    """
    All Courses including following fields
    """

    # uuid is used for external access hack prevention
    # Good for postgreSQL as it supports UUID Field
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    # Multiple courses can share the same subject.
    subject = models.ForeignKey(SubjectPossibleValues, on_delete=models.CASCADE)
    number = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    # Multiple courses can share the same details? This can be changed to OneToOneField.
    details = models.ForeignKey(CourseDetail, on_delete=models.CASCADE)

    def __str__(self):
        return (
                "Subject \t"
                + self.subject.__str__()
                + "\n"
                + "Number \t"
                + self.number.__str__()
                + "\n"
                + "Name \t"
                + self.name.__str__()
                + "\n"
                + "Detail \t ---------------- \n"
                + self.details.__str__()
        )



class Log(models.Model):
    """
    Not serialized.
    """

    time = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    message = models.TextField()
