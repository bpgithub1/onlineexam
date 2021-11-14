# Generated by Django 3.2 on 2021-08-13 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210808_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='institute_created_date',
            field=models.DateTimeField(default=datetime.date(2021, 8, 13)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_expiry_date',
            field=models.DateTimeField(default=datetime.date(2021, 11, 11)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='account_expiry_date',
            field=models.DateTimeField(default=datetime.date(2022, 8, 13)),
        ),
    ]