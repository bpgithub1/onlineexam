# Generated by Django 3.2 on 2021-09-21 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_alter_department_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 10, 4, 9, 982373)),
        ),
    ]
