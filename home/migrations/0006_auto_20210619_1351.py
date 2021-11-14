# Generated by Django 3.2 on 2021-06-19 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210618_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute_user',
            name='verify_id',
        ),
        migrations.AddField(
            model_name='institute_user',
            name='verification_id',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AddField(
            model_name='institute_user',
            name='verification_id_type',
            field=models.CharField(default='N/A', max_length=25),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_created_date',
            field=models.DateTimeField(default=datetime.date(2021, 6, 19)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_expiry_date',
            field=models.DateTimeField(default=datetime.date(2021, 9, 17)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='account_expiry_date',
            field=models.DateTimeField(default=datetime.date(2022, 6, 19)),
        ),
    ]
