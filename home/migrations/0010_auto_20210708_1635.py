# Generated by Django 3.2 on 2021-07-08 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210630_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ref_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='NA', max_length=5)),
                ('level', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ref_Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='NA', max_length=5)),
                ('subject', models.CharField(default='NA', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_created_date',
            field=models.DateTimeField(default=datetime.date(2021, 7, 8)),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_expiry_date',
            field=models.DateTimeField(default=datetime.date(2021, 10, 6)),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='account_expiry_date',
            field=models.DateTimeField(default=datetime.date(2022, 7, 8)),
        ),
    ]
