# Generated by Django 3.2 on 2021-08-17 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210817_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute_user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 20, 59, 48, 299435)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 17, 20, 59, 48, 298435)),
        ),
    ]