# Generated by Django 3.2 on 2021-09-21 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20210917_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automated_script',
            name='script_execution_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 966766)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_created_date',
            field=models.DateTimeField(default=datetime.date(2021, 9, 21)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_expiry_date',
            field=models.DateTimeField(default=datetime.date(2021, 12, 20)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 966766)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='joining_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 966766)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 966766)),
        ),
        migrations.AlterField(
            model_name='user_extra_info',
            name='account_expiry_date',
            field=models.DateTimeField(default=datetime.date(2022, 9, 21)),
        ),
        migrations.AlterField(
            model_name='user_extra_info',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 966766)),
        ),
    ]
