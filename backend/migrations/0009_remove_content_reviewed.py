# Generated by Django 3.0.4 on 2021-07-29 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20210728_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='reviewed',
        ),
    ]