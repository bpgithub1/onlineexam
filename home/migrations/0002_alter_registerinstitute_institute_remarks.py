# Generated by Django 3.2 on 2021-06-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerinstitute',
            name='institute_remarks',
            field=models.CharField(default='New Registration', max_length=250),
        ),
    ]
