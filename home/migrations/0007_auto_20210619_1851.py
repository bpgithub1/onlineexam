# Generated by Django 3.2 on 2021-06-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210619_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute_user',
            name='institute_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='contact1',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='institute_user',
            name='contact2',
            field=models.CharField(blank=True, default='N/A', max_length=100),
        ),
    ]
