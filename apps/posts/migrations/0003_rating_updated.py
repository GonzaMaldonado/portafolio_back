# Generated by Django 4.2.3 on 2023-08-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
