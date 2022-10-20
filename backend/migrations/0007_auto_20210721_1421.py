# Generated by Django 3.0.4 on 2021-07-21 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20210719_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='published_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Archive', 'Archive'), ('Deaccession', 'Deaccession'), ('Review', 'Review')], default='Review', max_length=32),
        ),
    ]