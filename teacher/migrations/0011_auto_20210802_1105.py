# Generated by Django 3.2 on 2021-08-02 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0010_rename_exam_question_question_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(default=datetime.date(2021, 10, 31)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(default=datetime.date(2021, 8, 2)),
        ),
    ]
