from django import forms
from django.db.models import fields
from django.db.models.fields import files
from home.models import Institute, User_Extra_Info
from django.contrib.auth.models import User

#get fields from Model-Institute Registration
class RegisterInstituteForm(forms.ModelForm):
    class Meta:
        model=Institute
        fields=[
            'institute_name',
            'institute_owner',
            'institute_contact1',
            'institute_contact2',
            'institute_email',
            'institute_country',
            'institute_state',
            'institute_city',
            'institute_address',
            'institute_pin_code',
            'institute_logo_path'            
        ]
        labels={'institute_logo_path':'Institute Logo',
                'institute_name':'Institute Name',
                'institute_owner':'Institute Owner',
                'institute_contact1':'Institute Contact',
                'institute_contact2':'',
                'institute_email':'Institute eMail',
                'institute_country':'Institute Country',
                'institute_state':'Institute State',
                'institute_city':'Institute City',
                'institute_address':'Institute Address',
                'institute_pin_code':'Institute PIN Code',
                
                
        }
       
        

#get fields for Django provided User Model
class UserInfoForm(forms.Form):
    email=forms.EmailField()    
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    first_name=forms.CharField(max_length=50,required=True)
    last_name=forms.CharField(max_length=50,required=True)
    


#get fields from Model - User Extra Information
class UserExtraInfoForm(forms.ModelForm):
    class Meta():
        model=User_Extra_Info
        fields=['contact1','contact2','verification_id','address','profile_pic_path'] 
        labels={'profile_pic_path':'Profile Photo',}       