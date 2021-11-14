# Generated by Django 3.2 on 2021-09-16 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0032_auto_20210916_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_released',
            old_name='IS_PROCESSED_BY_AUTO_SCRIPT',
            new_name='IS_PROCESSED_BY_SCRIPT',
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 403865)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 402864)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 400867)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 400867)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 401865)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 401865)),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 402864)),
        ),
        migrations.AlterField(
            model_name='question_marks',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 401865)),
        ),
        migrations.AlterField(
            model_name='question_options',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 19, 34, 23, 402864)),
        ),
    ]
