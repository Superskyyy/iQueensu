# Generated by Django 3.0.3 on 2020-02-06 22:34
from django.contrib.postgres.operations import TrigramExtension

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("QCumber", "0001_initial")]

    operations = [TrigramExtension()]