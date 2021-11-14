# Generated by Django 3.2 on 2021-07-08 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='20991231E9999', max_length=25)),
                ('start_date', models.DateTimeField(default=datetime.date(2021, 7, 8))),
                ('end_date', models.DateTimeField(default=datetime.date(2021, 10, 6))),
                ('is_released', models.CharField(max_length=1)),
                ('duration', models.IntegerField(default=0)),
                ('subject_code', models.CharField(default='NA', max_length=5)),
                ('level_code', models.CharField(default='NA', max_length=5)),
                ('institute_id', models.IntegerField(default=0)),
            ],
        ),
    ]