from django.db import models
# Create your models here.


# These table are claimed for better performance
class CareerPossibleValues(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class SubjectPossibleValues(models.Model):
    code = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.code + " - " + self.name


class CampusPossibleValues(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class GradingPossibleValues(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class AcademicGroupPossibleValues(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class AcademicOrganizationPossibleValues(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


# these tables are for separating the data
class Components(models.Model):
    description = models.TextField(null=True)

    def __str__(self):
        return self.description


class EnrollmentInformation(models.Model):
    description = models.TextField(null=True)

    def __str__(self):
        return self.description


class CourseDescription(models.Model):
    description = models.TextField(null=True)

    def __str__(self):
        return self.description


# actual representative tables
class CourseDetail(models.Model):
    career = models.ForeignKey(
        CareerPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    units = models.DecimalField(max_digits=4, decimal_places=2)
    grading_basis = models.ForeignKey(
        GradingPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    course_components = models.ForeignKey(
        Components,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    campus = models.ForeignKey(
        CampusPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    academic_group = models.ForeignKey(
        AcademicGroupPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    academic_organization = models.ForeignKey(
        AcademicOrganizationPossibleValues,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    enrollment = models.ForeignKey(
        EnrollmentInformation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    description = models.ForeignKey(
        CourseDescription,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return "Career \t" + self.career.__str__() + '\n' + \
               "Units \t" + self.units.__str__() + '\n' + \
               "Grading Basis \t" + self.grading_basis.__str__() + '\n' + \
               "Course Components \t" + self.course_components.__str__() + '\n' + \
               "Campus \t" + self.campus.__str__() + '\n' + \
               "Academic Group \t" + self.academic_group.__str__() + '\n' + \
               "Academic Organization \t" + self.academic_organization.__str__() + '\n' + \
               "Enrollment Information \t" + self.enrollment.__str__() + '\n' + \
               "Description \t" + self.description.__str__()


class Course(models.Model):
    subject = models.ForeignKey(
        SubjectPossibleValues,
        on_delete=models.CASCADE,
    )
    number = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    details = models.ForeignKey(
        CourseDetail,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Subject \t" + self.subject.__str__() + '\n' + \
               "Number \t" + self.number.__str__() + '\n' + \
               "Name \t" + self.name.__str__() + '\n' + \
               "Detail \t ---------------- \n" + self.details.__str__()


class Log(models.Model):
    time = models.DateTimeField(auto_now=True, auto_now_add=True)
    source = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    message = models.TextField()
