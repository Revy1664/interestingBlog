# Generated by Django 5.0.4 on 2024-04-16 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 16, 13, 20, 53, 657945, tzinfo=datetime.timezone.utc)),
        ),
    ]