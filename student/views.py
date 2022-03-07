#Latest Change:request.is_ajax(): #removed as it is depricated in django 4.0
from django.shortcuts import render
from django.http.response import JsonResponse
from django.db import connection

from home.views import getInstituteDbId, getUserDbId
from teacher.models import EXAM_ATTENDENCE 

#------------------------functions----------
#-------Get All Available Exams List --------
def get_available_exams(request):    
    if request.method=='POST':#and request.is_ajax():
        vUserLoginId=request.user 
        vUserDbId=getUserDbId(vUserLoginId)
        vInstDbId=getInstituteDbId(vUserLoginId) 
        cursor=connection.cursor()
        cursor.execute('''
            select 
                b.institute_name,
                a.euid as exam_code, 
                c.subject,
                a.full_marks as total_marks,
                a.total_questions,
                d.level,
                e.section, 
                a.sch_end_date,
                a.attend_status_desc
            from 
                teacher_exam_attendence a, 
                home_institute b, 
                home_ref_subject c,
                home_ref_level d,
                home_ref_section e
            where 1=1
                and a.institute_id=b.id
                and a.subject_code=c.code
                and a.level_code=d.code
                and a.section_code=e.code
                and student_id=
        '''+str(vUserDbId))
        
        result=cursor.fetchall()  
        connection.close()
        # vQsExam=EXAM_ATTENDENCE.objects.values().filter().order_by('uid') 
        # # vExamList=list(vQsExam)     
        print("bp---->",vUserDbId,"----",result)                        
        return JsonResponse ({'djStatus':1,'djExamList':result}) 


def setcookie(request): #only for RnD
    pass
    
