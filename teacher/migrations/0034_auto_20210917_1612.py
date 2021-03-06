# Generated by Django 3.2 on 2021-09-17 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0033_auto_20210916_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_released',
            old_name='IS_PROCESSED_BY_SCRIPT',
            new_name='is_processed_by_script',
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(default=datetime.date(2021, 12, 16)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(default=datetime.date(2021, 9, 17)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='sch_end_date',
            field=models.DateTimeField(default=datetime.date(2021, 12, 16)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='sch_start_date',
            field=models.DateTimeField(default=datetime.date(2021, 9, 17)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='sch_end_date',
            field=models.DateTimeField(default=datetime.date(2021, 12, 16)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='sch_start_date',
            field=models.DateTimeField(default=datetime.date(2021, 9, 17)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='question_marks',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
        migrations.AlterField(
            model_name='question_options',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 16, 12, 20, 383388)),
        ),
    ]
