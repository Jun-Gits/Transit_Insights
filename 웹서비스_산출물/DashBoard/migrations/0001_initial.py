# Generated by Django 4.2.5 on 2023-09-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVForHeatmapTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Station', models.CharField(max_length=255)),
                ('Time_06', models.FloatField()),
                ('Time_07', models.FloatField()),
                ('Time_08', models.FloatField()),
                ('Time_09', models.FloatField()),
                ('Time_10', models.FloatField()),
                ('Time_11', models.FloatField()),
                ('Time_12', models.FloatField()),
                ('Time_13', models.FloatField()),
                ('Time_14', models.FloatField()),
                ('Time_15', models.FloatField()),
                ('Time_16', models.FloatField()),
                ('Time_17', models.FloatField()),
                ('Time_18', models.FloatField()),
                ('Time_19', models.FloatField()),
                ('Time_20', models.FloatField()),
                ('Time_21', models.FloatField()),
                ('Time_22', models.FloatField()),
                ('Time_23', models.FloatField()),
            ],
        ),
    ]
