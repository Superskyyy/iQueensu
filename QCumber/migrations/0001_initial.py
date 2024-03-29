# Generated by Django 3.0.3 on 2020-02-06 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AcademicGroupPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("academic_group", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="AcademicOrganizationPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("academic_organization", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="CampusPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("campus", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="CareerPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("career", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Components",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseDescription",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="EnrollmentInformation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("enroll_add_consent", models.TextField(null=True)),
                ("enroll_drop_consent", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GradingPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grading", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="LearningHours",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("learning_hours", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now=True)),
                ("source", models.CharField(max_length=128)),
                ("type", models.CharField(max_length=32)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SubjectPossibleValues",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="CourseDetail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("units", models.TextField(null=True)),
                (
                    "academic_group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.AcademicGroupPossibleValues",
                    ),
                ),
                (
                    "academic_organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.AcademicOrganizationPossibleValues",
                    ),
                ),
                (
                    "campus",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="campus_names",
                        to="QCumber.CampusPossibleValues",
                    ),
                ),
                (
                    "career",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.CareerPossibleValues",
                    ),
                ),
                (
                    "course_components",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.Components",
                    ),
                ),
                (
                    "description",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.CourseDescription",
                    ),
                ),
                (
                    "enrollment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.EnrollmentInformation",
                    ),
                ),
                (
                    "grading_basis",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.GradingPossibleValues",
                    ),
                ),
                (
                    "learning_hours",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="QCumber.LearningHours",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=128)),
                ("name", models.CharField(max_length=128)),
                (
                    "details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="QCumber.CourseDetail",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="QCumber.SubjectPossibleValues",
                    ),
                ),
            ],
        ),
    ]