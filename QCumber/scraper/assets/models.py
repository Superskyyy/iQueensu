"""
This is the models for QCumber courses,
Only Course and CourseDetails are serialized.
"""
import uuid

from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.


# These table are claimed for better performance
class CareerPossibleValues(models.Model):
    """
    Career table for reusable entries
    """

    career = models.CharField(max_length=128)

    def __str__(self):
        return self.career


class SubjectPossibleValues(models.Model):
    """
    Subject table for reusable entries, this table contains the subject code + name
    """

    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.code + " - " + self.name


class CampusPossibleValues(models.Model):
    """
    Campus, e.g. Main
    """

    campus = models.CharField(max_length=128)

    def __str__(self):
        return self.campus


class GradingPossibleValues(models.Model):
    """
    Grading. E.g. "grading": "Pass/Fail",
    """

    grading = models.CharField(max_length=128)

    def __str__(self):
        return self.grading


class AcademicGroupPossibleValues(models.Model):
    """
    E.g. "academic_group": "School of Graduate Studies",
    """

    academic_group = models.CharField(max_length=128)

    def __str__(self):
        return self.academic_group


class AcademicOrganizationPossibleValues(models.Model):
    """
    E.g. "academic_organization": "REH (not department specific)",
    """

    academic_organization = models.CharField(max_length=128)

    def __str__(self):
        return self.academic_organization


class Components(models.Model):
    """
    E.g. "components": "Seminar",
    """

    description = models.TextField(null=True)

    def __str__(self):
        return self.description


class EnrollmentInformation(models.Model):
    """
    E.g.
    "enroll_add_consent": "Department Consent Required",
    "enroll_drop_consent": "Department Consent Required",
    """

    enroll_add_consent = models.TextField(null=True)
    enroll_drop_consent = models.TextField(null=True)

    def __str__(self):
        return self.enroll_add_consent + "-" + self.enroll_drop_consent


class LearningHours(models.Model):
    """
    E.g.
    "learning_hours": "144 (48Lb;96P)",
    """

    learning_hours = models.TextField(null=True)

    def __str__(self):
        return self.learning_hours or ""  ## This line without '' causes NONETYPE


class CourseDescription(models.Model):
    """
    Simply course description as a Text.
    """

    description = models.TextField(null=True)

    def __str__(self):
        return self.description


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
        print(
            (
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
        )
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
    details = models.OneToOneField(CourseDetail, on_delete=models.CASCADE)

    def __str__(self):
        print(
            (
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
        )
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


class CourseRating(models.Model):
    """
    This is the model for reviews and comments on the course

    Relations:
    Each course have multiple CourseReviews
    CourseReview <- foreign key -> Course
    Each course can have only one star rating
    One on one relation

    E.g.
    "course_review": "This Queen's Course is just perfect",
    """
    # the semester of the class
    year = models.IntegerField(validators=[MinValueValidator(2014), MaxValueValidator(datetime.date.today().year + 1)],
                               default=datetime.date.today().year)
    TERM_IN_SCHOOL_CHOICES = [('FALL', "Fall"), ('WINTER', "Winter"), ('SUMMER', "Summer")]
    term = models.CharField(
        max_length=50,
        choices=TERM_IN_SCHOOL_CHOICES,
        default='FALL',
    )

    # professor (display the profs in the specific faculty), or just write down the name
    # PROF_CHOICES = [('SELECT', "Please select"), ('YUANTIAN', "Yuan Tian"), ('TINGHU', "Ting Hu")]
    # prof = models.CharField(
    #     max_length=50,
    #     choices=PROF_CHOICES,
    #     default='SELECT',
    #     blank=True,
    # )
    prof = models.CharField(max_length=128, blank=True)

    course_review = models.TextField(null=True)
    star_ratings = models.SmallIntegerField()
    # where do we need the star rating
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)

    # Be very careful on the comments we don't want the comments to lose

    # Now here we also want to relate to User model

    def __str__(self):
        return self.course_review

