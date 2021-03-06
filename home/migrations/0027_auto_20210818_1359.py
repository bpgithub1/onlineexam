# Generated by Django 3.2 on 2021-08-18 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20210818_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institute_user',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='user_extra_info',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 13, 59, 49, 265872)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 13, 59, 49, 265872)),
        ),
        migrations.AlterField(
            model_name='user_extra_info',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 13, 59, 49, 265872)),
        ),
    ]
