# Generated by Django 3.0.4 on 2022-07-21 17:31

import backend.models
import backend.validators
import datetime
from django.db import migrations, models
import django_clamd.validators


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_content_original_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_file',
            field=models.FileField(max_length=500, upload_to=backend.models.Content.set_file_name, validators=[backend.validators.validate_unique_filename, django_clamd.validators.validate_file_infection, backend.validators.validate_file_size], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='copyrightpermission',
            name='date_of_response',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
