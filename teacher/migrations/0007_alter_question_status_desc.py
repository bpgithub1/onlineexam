# Generated by Django 3.2 on 2021-07-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_alter_question_status_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status_desc',
            field=models.CharField(default='Active', max_length=50),
        ),
    ]