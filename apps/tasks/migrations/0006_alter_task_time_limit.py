# Generated by Django 4.2.3 on 2023-08-23 17:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_time_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_limit',
            field=models.DateTimeField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(datetime.datetime(2023, 8, 23, 14, 46, 37, 296750))]),
        ),
    ]