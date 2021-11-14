from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime,timedelta


# Create your models here.
#-------------------------------------------------
class Ref_UID(models.Model):
    uid=models.CharField(max_length=20,default='NA')
    table_code=models.CharField(max_length=5,default='NA')
    table_name=models.CharField(max_length=100,default='NA')

#--------------------------------------------------
class Ref_Subject(models.Model):
    code=models.CharField(max_length=5,default='NA')
    subject=models.CharField(max_length=100,default='NA')

class Ref_Level(models.Model):
    code=models.CharField(max_length=5,default='NA')
    level=models.CharField(max_length=100,default='NA')

class Ref_Section(models.Model):
    code=models.CharField(max_length=5,default='NA')
    section=models.CharField(max_length=100,default='NA')

class Automated_Script(models.Model):
    script_name=models.CharField(max_length=100,default='N/A')
    script_name_desc=models.CharField(max_length=100,default='N/A')
    script_execution_date=models.DateTimeField(default=datetime.today())
    script_execution_mode=models.CharField(max_length=100,default='N/A')
    script_action=models.CharField(max_length=100,default='N/A')
    script_execution_status=models.CharField(max_length=100,default='N/A')
    

class Institute(models.Model):
    institute_name=models.CharField(max_length=100)
    institute_owner=models.CharField(max_length=100)
    institute_contact1=models.CharField(max_length=100)
    institute_contact2=models.CharField(max_length=100,default="N/A")
    institute_email=models.EmailField()
    institute_country=models.CharField(max_length=100)
    institute_state=models.CharField(max_length=100)
    institute_city=models.CharField(max_length=100)
    institute_address=models.CharField(max_length=250)
    institute_pin_code=models.IntegerField(default=100100)
    institute_status=models.CharField(default="InActive",max_length=25)
    institute_created_date=models.DateTimeField(default=date.today())
    institute_expiry_date=models.DateTimeField(default=date.today()+timedelta(days=90))
    institute_remarks=models.CharField(max_length=250,default="New Registration")
    institute_logo_path=models.ImageField(upload_to="logo",default="")
    institute_updated_date=models.DateTimeField(default=datetime.today())

class User_Extra_Info(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #-----add more properties---------
    #the table (auth_user) will be joined by django with home_user_extra_info by key user based on one-to-one relationship
    #django by default adds _id in user hence this becomes ===> user_id
    contact1=models.CharField(max_length=100,default="N/A")
    contact2=models.CharField(max_length=100,default="N/A",blank=True)
    #user_created_date=models.DateTimeField(default=date.today(),auto_now_add=True)
    #user_created_date=models.DateTimeField(auto_now_add=True) #this field is already available in Django provided auth_user(date_joined)  
    account_expiry_date=models.DateTimeField(default=date.today()+timedelta(days=365))
    remarks=models.CharField(max_length=250,default="New Individual Registration")
    type=models.CharField(default="N/A",max_length=25)
    verification_id_type=models.CharField(max_length=25,default="N/A")
    verification_id=models.CharField(max_length=25,default="N/A")
    address=models.CharField(max_length=250,default="N/A")
    # institute_id=models.IntegerField(default=0)
    profile_pic_path=models.ImageField(upload_to="profile",default="")
    updated_date=models.DateTimeField(default=datetime.today())
    status=models.CharField(max_length=25,default="N/A")

class Institute_User(models.Model):
    user_id=models.IntegerField(default=0)
    institute_id=models.IntegerField(default=0)
    updated_date=models.DateTimeField(default=datetime.today())
    joining_date=models.DateTimeField(default=datetime.today())

# class Institute_User(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     #-----add more properties---------
#     #the table (auth_user) will be joined by django with home_institute_user by key user_id based on one-to-one relationship
#     contact1=models.CharField(max_length=100,default="N/A")
#     contact2=models.CharField(max_length=100,default="N/A",blank=True)
#     #user_created_date=models.DateTimeField(default=date.today(),auto_now_add=True)
#     #user_created_date=models.DateTimeField(auto_now_add=True) #this field is already available in Django provided auth_user(date_joined)  
#     account_expiry_date=models.DateTimeField(default=date.today()+timedelta(days=365))
#     remarks=models.CharField(max_length=250,default="New Individual Registration")
#     type=models.CharField(default="N/A",max_length=25)
#     verification_id_type=models.CharField(max_length=25,default="N/A")
#     verification_id=models.CharField(max_length=25,default="N/A")
#     address=models.CharField(max_length=250,default="N/A")
#     institute_id=models.IntegerField(default=0)
#     profile_pic_path=models.ImageField(upload_to="profile",default="")
#     updated_date=models.DateTimeField(default=datetime.today())
#     status=models.CharField(max_length=25,default="N/A")

    def __str__(self):
        return self.user.username #user has username field