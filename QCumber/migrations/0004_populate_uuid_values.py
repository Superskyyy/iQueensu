"""
DO NO MODIFY UNLESS YOU KNOW WHAT YOU ARE DOING
This module adds uuid field, with the help of 0003 0004 0005
https://docs.djangoproject.com/en/3.0/howto/
writing-migrations/#migrations-that-add-unique-fields
"""
import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    course_model = apps.get_model("QCumber", "course")
    for row in course_model.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


class Migration(migrations.Migration):
    dependencies = [("QCumber", "0003_add_uuid_field")]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop)
    ]
