# Generated by Django 3.0.3 on 2020-02-18 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QCumber', '0007_auto_20200218_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserating',
            name='prof',
            field=models.CharField(choices=[(1, 'Please select'), (2, 'Yuan Tian'), (3, 'Ting Hu')], default=1, max_length=2),
        ),
    ]
