# Generated by Django 4.2.3 on 2023-08-13 16:05

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0004_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(datetime.date(2023, 8, 13))]),
        ),
    ]