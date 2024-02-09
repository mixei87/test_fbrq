# Generated by Django 5.0.1 on 2024-01-31 18:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='code',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(900), django.core.validators.MaxValueValidator(999)]),
        ),
    ]