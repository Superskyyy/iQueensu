"""
This module enables trigram similarity extension in PostgreSQL
"""
from django.contrib.postgres.operations import TrigramExtension

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("QCumber", "0001_initial")]

    operations = [TrigramExtension()]
