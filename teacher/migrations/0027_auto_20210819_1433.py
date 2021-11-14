# Generated by Django 3.2 on 2021-08-19 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0026_auto_20210818_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 33, 5, 141785)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(default=datetime.date(2021, 11, 17)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(default=datetime.date(2021, 8, 19)),
        ),
        migrations.AlterField(
            model_name='exam',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 33, 5, 141785)),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 33, 5, 141785)),
        ),
        migrations.AlterField(
            model_name='question_marks',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 33, 5, 137774)),
        ),
        migrations.AlterField(
            model_name='question_options',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 14, 33, 5, 141785)),
        ),
    ]
