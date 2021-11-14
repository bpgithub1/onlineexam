# Generated by Django 3.2 on 2021-09-16 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20210916_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automated_script',
            name='script_execution_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 33, 28, 497407)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 33, 28, 497407)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='joining_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 33, 28, 498406)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 33, 28, 498406)),
        ),
        migrations.AlterField(
            model_name='user_extra_info',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 33, 28, 498406)),
        ),
    ]
