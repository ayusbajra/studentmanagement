# Generated by Django 5.0.6 on 2024-06-22 14:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='exam_score',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
