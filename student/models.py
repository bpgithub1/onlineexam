from django.db import models
from datetime import date, datetime,timedelta

# Create your models here.
class Department(models.Model):
    user_id=models.IntegerField(default=0)
    level_id=models.CharField(max_length=5,default='NA')
    section_id=models.CharField(max_length=5,default='NA')
    institute_id=models.IntegerField(default=0)
    updated_date=models.DateTimeField(default=datetime.today())