from django.db import models
from datetime import date, datetime,timedelta

# Create your models here.

#-----Exam Attendence Data------
class EXAM_ATTENDENCE(models.Model):
    euid=models.CharField(max_length=25,default="20991231E9999")
    institute_id=models.IntegerField(default=0)
    level_code=models.CharField(max_length=5,default='NA')
    subject_code=models.CharField(max_length=5,default='NA')
    section_code=models.CharField(max_length=5,default='NA')
    updated_date=models.DateTimeField(default=datetime.today())
    student_id=models.IntegerField(default=0) # Attendence need by student 
    created_date=models.DateTimeField(default=datetime.today())
    attend_status=models.CharField(max_length=5,default="N")
    attend_status_desc=models.CharField(max_length=100,default="Not Yet Attended By Student")    
    sch_start_date=models.DateTimeField(default=date.today())
    sch_end_date=models.DateTimeField(default=date.today()+timedelta(days=90))
    full_marks=models.IntegerField(default=0)
    scored_marks=models.IntegerField(default=0)
    duration=models.IntegerField(default=0)
    total_questions=models.IntegerField(default=0)  
    total_attended_questions=models.IntegerField(default=0)  
    exam_attend_date=models.DateTimeField(default='2020-01-01 00:00:00')
    exam_completion_date=models.DateTimeField(default='2020-01-01 00:00:00')  
    entry_source=models.CharField(max_length=100,default="NA")

    


#-----Only Released Exam Data------
class EXAM_RELEASED(models.Model):
    euid=models.CharField(max_length=25,default="20991231E9999")
    institute_id=models.IntegerField(default=0)
    level_code=models.CharField(max_length=5,default='NA')
    subject_code=models.CharField(max_length=5,default='NA')
    section_code=models.CharField(max_length=5,default='NA')
    updated_date=models.DateTimeField(default=datetime.today())
    released_by=models.IntegerField(default=0) # Released By User Id
    created_date=models.DateTimeField(default=datetime.today())
    sch_start_date=models.DateTimeField(default=date.today())
    sch_end_date=models.DateTimeField(default=date.today()+timedelta(days=90))
    full_marks=models.IntegerField(default=0)
    duration=models.IntegerField(default=0)
    total_questions=models.IntegerField(default=0)    
    status=models.CharField(max_length=25,default="OPEN")
    status_desc=models.CharField(max_length=100,default="Released Exam - Open To Participant")
    is_processed_by_script=models.CharField(max_length=5,default='NO')
    


#-----Exam-Question Related Data------
class Question_Marks(models.Model):
    euid=models.CharField(max_length=25,default="20991231E9999")
    quid=models.CharField(max_length=25,default="20991231Q9999")
    institute_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    marks=models.IntegerField(default=1)
    subject_id=models.CharField(max_length=5,default='NA')
    updated_date=models.DateTimeField(default=datetime.today())

#-----Question-Options Related Data------
class Question_Options(models.Model):
    quid=models.CharField(max_length=25,default="20991231Q9999")
    tag=models.CharField(max_length=1,default="X")
    particulars=models.CharField(max_length=250,default='Question Option Particulars')
    is_correct=models.IntegerField(default=0)
    institute_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    updated_date=models.DateTimeField(default=datetime.today())
    
#-----Only Exam Related Data------
class Exam(models.Model):
    uid=models.CharField(max_length=25,default="20991231E9999")
    start_date=models.DateTimeField(default=date.today())
    end_date=models.DateTimeField(default=date.today()+timedelta(days=90))
    is_released=models.CharField(max_length=5,default=0)
    duration=models.IntegerField(default=0)
    subject_code=models.CharField(max_length=5,default='NA')
    level_code=models.CharField(max_length=5,default='NA')
    section_code=models.CharField(max_length=5,default='NA')
    institute_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    type_code=models.CharField(max_length=5,default=0)
    type_desc=models.CharField(max_length=100,default=0)
    source_code=models.CharField(max_length=5,default='NA')#--FRS, CPY, RER
    source_desc=models.CharField(max_length=100,default='')#--Freshly Created Exam, Copied Exam, Re-Releaded Exam    
    source_uid=models.CharField(max_length=25,default="20991231E9999")
    updated_date=models.DateTimeField(default=datetime.today())
    
#-----Only Question Related Data------
class Question(models.Model):
    uid=models.CharField(max_length=25,default="20991231Q9999")
    institute_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    level_code=models.CharField(max_length=5,default='NA')
    subject_code=models.CharField(max_length=5,default='NA')
    particulars=models.CharField(max_length=250,default='Question Particulars')
    status=models.IntegerField(default=1)
    status_desc=models.CharField(max_length=50,default='Active')
    image_path=models.ImageField(upload_to="question",default="")
    type=models.IntegerField(default=1)
    type_desc=models.CharField(max_length=100,default='')    
    answer=models.CharField(max_length=250,default='Answer for Reference')
    updated_date=models.DateTimeField(default=datetime.today())
    
class Department(models.Model):
    user_id=models.IntegerField(default=0)
    institute_id=models.IntegerField(default=0)
    subject_id=models.CharField(max_length=5,default='NA')
    updated_date=models.DateTimeField(default=datetime.today())


