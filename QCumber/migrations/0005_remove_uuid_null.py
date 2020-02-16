"""
DO NO MODIFY UNLESS YOU KNOW WHAT YOU ARE DOING
This module adds uuid field, with the help of 0003 0004 0005
https://docs.djangoproject.com/en/3.0/howto/
writing-migrations/#migrations-that-add-unique-fields
"""

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("QCumber", "0004_populate_uuid_values")]

    operations = [
        migrations.RemoveField(model_name="course", name="id"),
        migrations.AlterField(
            model_name="course",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
