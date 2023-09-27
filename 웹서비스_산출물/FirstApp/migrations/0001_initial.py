# Generated by Django 4.2.4 on 2023-09-06 04:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCsv_Subway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SW_ID', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('SW_Station', models.CharField(blank=True, max_length=100, null=True)),
                ('SW_Num', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
