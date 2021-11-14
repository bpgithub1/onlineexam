# Generated by Django 3.2 on 2021-09-21 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0035_auto_20210921_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_attendence',
            name='entry_source',
            field=models.CharField(default='Nil', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 546963)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 546963)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 544919)),
        ),
        migrations.AlterField(
            model_name='exam_attendence',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 544919)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 545953)),
        ),
        migrations.AlterField(
            model_name='exam_released',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 545953)),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 546963)),
        ),
        migrations.AlterField(
            model_name='question_marks',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 545953)),
        ),
        migrations.AlterField(
            model_name='question_options',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 13, 8, 48, 545953)),
        ),
    ]
