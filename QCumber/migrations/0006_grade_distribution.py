"""
create gradeDistribution table
"""
# Generated by Django 3.0.3 on 2020-03-01 21:11

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """migration"""
    dependencies = [
        ('QCumber', '0005_remove_uuid_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradeDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
