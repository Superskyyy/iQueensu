"""
DO NO MODIFY UNLESS YOU KNOW WHAT YOU ARE DOING
This module adds uuid field, with the help of 0003 0004 0005
https://docs.djangoproject.com/en/3.0/howto/
writing-migrations/#migrations-that-add-unique-fields
"""
import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("QCumber", "0002_trigram_support")]

    operations = [
        migrations.AddField(
            model_name="course",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, null=True),
        )
    ]
