# Generated by Django 3.2 on 2021-06-14 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterInstitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100)),
                ('institute_owner', models.CharField(max_length=100)),
                ('institute_contact1', models.CharField(max_length=100)),
                ('institute_contact2', models.CharField(max_length=100)),
                ('institute_email', models.EmailField(max_length=254)),
                ('institute_country', models.CharField(max_length=100)),
                ('institute_state', models.CharField(max_length=100)),
                ('institute_city', models.CharField(max_length=100)),
                ('institute_address', models.CharField(max_length=250)),
                ('institute_pin_code', models.IntegerField()),
                ('institute_status', models.CharField(default='Active', max_length=25)),
                ('institute_created_date', models.DateTimeField(default=datetime.date(2021, 6, 14))),
                ('institute_expiry_date', models.DateTimeField(default=datetime.date(2021, 9, 12))),
                ('institute_remarks', models.CharField(max_length=250)),
            ],
        ),
    ]
