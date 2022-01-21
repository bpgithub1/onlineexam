#---DJANGO
from django.shortcuts import render
from django.shortcuts import render,HttpResponse, resolve_url
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import connection

#-----Generic USE
from typing import List
import json
import os
import re

#-----MODELS
from home.models import Institute, Ref_Level, Ref_Section,Ref_Subject,Ref_UID,Institute_User, User_Extra_Info
from teacher.models import Exam,EXAM_RELEASED,EXAM_ATTENDENCE, Question,Question_Marks, Question_Options, Department as TeacherDeparment
from student.models import Department as StudentDepartment

#----VIEWS
from home.views import getLevelSectionList,getSubjectList,getUserDbId,getInstituteDbId


#----COMMON FUNCITONS
from onlineexam.common import getNewPrimaryKey

#----SETTING
from onlineexam import global_variables, settings

from datetime import date, datetime,timedelta
import os
from onlineexam import settings

#==============FUNCTION DEFINITION=====================

#----save institute details-------
def save_institute_details(request):
    if request.method=='POST' :#and request.is_ajax():
        vStr=request.user
        vId=request.POST.get('hId')
        vName=request.POST.get('hName')
        vOwner=request.POST.get('hOwner')
        vEmail=request.POST.get('hEmail')
        vContact1=request.POST.get('hContact1')
        vContact2=request.POST.get('hContact2')
        vCountry=request.POST.get('hCountry')
        vState=request.POST.get('hState')
        vCity=request.POST.get('hCity')
        vAddress=request.POST.get('hAddress')
        vPinCode=request.POST.get('hPinCode')
        Institute.objects.filter(id=vId).update(                    
            institute_name=vName,
            institute_owner=vOwner,
            institute_email=vEmail,
            institute_contact1=vContact1,
            institute_contact2=vContact2,
            institute_country=vCountry,
            institute_state=vState,
            institute_city=vCity,
            institute_address=vAddress,
            institute_pin_code=vPinCode, 
            institute_remarks='Institute Edited Successfully',  
            institute_updated_date=datetime.today() 
        )                   
    return JsonResponse ({'djStatus':1}) 

#----save institute details (Image)-------
def save_institute_details_image(request):
    vStr=request.user
    vId=request.POST.get('hId')
    #------save image (if new image is coming then )
    vImageSrcNew = request.FILES.get('file_manage_institute_logo')  
    vQsImagePath=Institute.objects.values().filter(id=vId)
    vImagePathExisting=vQsImagePath[0]['institute_logo_path'] 
    #print("save image called. . ..")      
    vObjImage=Institute.objects.get(id=vId)   
    if vImageSrcNew is not None: 
        vObjImage.institute_logo_path=vImageSrcNew
        vObjImage.save()        
        os.remove(os.path.join(settings.MEDIA_ROOT, vImagePathExisting))
                         
    return JsonResponse ({'djStatus':1}) 

#-----Get Institute Data-----
def get_institute_data(request):
    #-----Retrieve details and return-----
    vStr=request.user
    vInstituteDbId=getInstituteDbId(vStr)
    vQsInstituteData=Institute.objects.values(
        'id',
        'institute_status',
        'institute_name',
        'institute_owner',
        'institute_email',
        'institute_contact1',
        'institute_contact2',
        'institute_country',
        'institute_state',
        'institute_city',
        'institute_address',
        'institute_pin_code',
        'institute_logo_path',        
        ).filter(id__exact=vInstituteDbId)
    vInstituteDataList=list(vQsInstituteData)     

    # print("bp----------",vInstituteDataList)   

    return JsonResponse ({'djStatus':1,'djInstituteDetails':vInstituteDataList})  


#-----SAVE TEACHER DATA
def save_teacher_data(request):
    if request.method=='POST' :#and request.is_ajax():
        vTeacherUserId=request.POST.get('hTeacherUserId') 
        vAction=request.POST.get('hAction') 
        vIsSubjectDefined=request.POST.get('hIsSubjectDefined')
        vSubject=""
        if(vIsSubjectDefined=="1"):
            pass
        else:
            vSubject=json.loads(request.POST['hSubject'], encoding="utf-8")
        print(vSubject)    
        vLoginId=request.user
        vLoginUserDbId=getUserDbId(vLoginId)
        vLoginInstDbId=getInstituteDbId(vLoginId)
        vTeacherDbId=getUserDbId(vTeacherUserId)     
        #---first remove all the rows of class and section of the student from institute (Admin's Institute)
        TeacherDeparment.objects.filter(user_id=vTeacherDbId,institute_id=vLoginInstDbId,).delete()
        #===Nothing to do for Action=1   
        if vAction=="2":
            #--Since teacher is always present in institute, only required to Activate/De-Activate
            user_info=User.objects.filter(id=vTeacherDbId).update(is_active=1) #---Update IS_ACTIVE=1 in USER table
            #user_info.save() #--this is not needed in case of update
            user_extra_info=User_Extra_Info.objects.filter(user_id=vTeacherDbId).update(status="Active") #---update STATUS='ACTIVE' in user_extra_info table
            #user_extra_info.save() #--this is not needed in case of update; we do not need to save explicitely
        elif vAction=="3": # ===when remove student from institute   
            user_info=User.objects.filter(id=vTeacherDbId).update(is_active=0) #---Update IS_ACTIVE=1 in USER table
            user_extra_info=User_Extra_Info.objects.filter(user_id=vTeacherDbId).update(status="InActive") #---update STATUS='ACTIVE' in user_extra_info table
        else:
            pass
        
        if vAction=="2" or vAction=="4":    
            for i in range(len(vSubject)):
                if i>0:                
                    vStudentDept=TeacherDeparment(  
                                user_id=vTeacherDbId,
                                institute_id=vLoginInstDbId,                                                        
                                subject_id=vSubject[i][1],                                
                            )                           
                    vStudentDept.save() 
            
        return JsonResponse ({'djStatus':1,})



#-----SAVE STUDENT DATA
def save_student_data(request):
    if request.method=='POST' :#and request.is_ajax():
        vStudentUserId=request.POST.get('hStudentUserId') 
        vAction=request.POST.get('hAction') 
        vIsLevelSectionDefined=request.POST.get('hIsLevelSectionDefined')
        vFlag=1 #if is assumed that admin is submitting right values
        vLevelSection=""
        if(vIsLevelSectionDefined=="1"):
            pass
        else:
            vLevelSection=json.loads(request.POST['hLevelSection'], encoding="utf-8")
        vLoginId=request.user
        vLoginUserDbId=getUserDbId(vLoginId)
        vLoginInstDbId=getInstituteDbId(vLoginId)
        vStudentDbId=getUserDbId(vStudentUserId)     
        


        #---first remove class and section of the student from institute (Admin's Institute)
        #StudentDepartment.objects.filter(user_id=vStudentDbId,institute_id=vLoginInstDbId,).delete()
        
        #---check level & section; delete those levels and section from the student department table which is not present in coming (from web) list  
        vQsStudentDept=StudentDepartment.objects.values().filter(institute_id__exact=vLoginInstDbId,user_id=vStudentDbId,)         
        vStudentDeptList=list(vQsStudentDept) 
        for vCursor in vStudentDeptList:             
            for i in range(len(vLevelSection)):
                if i>0: 
                    if vCursor['level_id']==vLevelSection[i][1] and vCursor['section_id']==vLevelSection[i][3]: 
                        pass
                    else:    
                        StudentDepartment.objects.filter(user_id=vStudentDbId,institute_id=vLoginInstDbId,level_id__exact=vCursor['level_id'],section_id__exact=vCursor['section_id']).delete()                      
                   
                                

        #-----------------------OPERATION 1--------------------   
        if vAction=="2": #when add stundent in the institute
            Institute_User.objects.filter(user_id=vStudentDbId,institute_id=vLoginInstDbId,).delete() #--Delete student entry if any present for that institute 
            user_institute_info = Institute_User(user_id=vStudentDbId,institute_id=vLoginInstDbId,joining_date=datetime.today()) #---Insert entry in institute_user table
            user_institute_info.save()
            user_info=User.objects.filter(id=vStudentDbId).update(is_active=1) #---Update IS_ACTIVE=1 in USER table
            #user_info.save() #--this is not needed in case of update
            user_extra_info=User_Extra_Info.objects.filter(user_id=vStudentDbId).update(status="Active") #---update STATUS='ACTIVE' in user_extra_info table
            #user_extra_info.save() #--this is not needed in case of update
        elif vAction=="3": # ===when remove student from institute   
            Institute_User.objects.filter(user_id=vStudentDbId,institute_id=vLoginInstDbId,).delete() #--Delete student entry if any present for that institute 
            user_info=User.objects.filter(id=vStudentDbId).update(is_active=0) #---Update IS_ACTIVE=1 in USER table
            user_extra_info=User_Extra_Info.objects.filter(user_id=vStudentDbId).update(status="InActive") #---update STATUS='ACTIVE' in user_extra_info table
            StudentDepartment.objects.filter(user_id=vStudentDbId,institute_id=vLoginInstDbId,).delete()
        else:
            pass
        #-----------------------OPERATION 2--------------------
        if vAction=="2" or vAction=="4": # when level and section is modified.   
            for i in range(len(vLevelSection)):
                if i>0:  
                    #----check the section and level is same as the what is stored in DB and what is comming; 
                    #----if both are same then no processing will take place.              
                    vResultCount=StudentDepartment.objects.values().filter(
                        institute_id__exact=vLoginInstDbId,
                        level_id__exact=vLevelSection[i][1],
                        section_id__exact=vLevelSection[i][3],
                        user_id=vStudentDbId,).count()
                    print("BP-->Level & Section Present Count:",vResultCount)    
                    if vResultCount>0: #count >0 means entry is already present    
                        pass
                    else: # insert entry in the department table
                        #update student department
                        vStudentDept=StudentDepartment(  
                                    user_id=vStudentDbId,
                                    institute_id=vLoginInstDbId,                                                        
                                    level_id=vLevelSection[i][1],
                                    section_id=vLevelSection[i][3],
                                )                           
                        vStudentDept.save() 
                        #-----Now insert all the available exam to this student, in attendance table 
                        #read from released exam
                        vQsReleasedExamData=EXAM_RELEASED.objects.values().filter(
                            institute_id__exact=vLoginInstDbId,
                            level_code__exact=vLevelSection[i][1],
                            section_code__exact=vLevelSection[i][3],
                            status__exact=global_variables.EXAM_RELEASED_STATUS_OPEN,
                            #sch_start_date__lte=datetime.today(),
                            sch_end_date__gte=datetime.today(),
                            ) 
                        print("BP===EXAM Data",vQsReleasedExamData)
                        #insert data in attendance table
                        vReleasedExamDataList=list(vQsReleasedExamData) 
                        for vCursor in vReleasedExamDataList:            
                            vObjReleasedExamAttendance=EXAM_ATTENDENCE(  
                                        euid=vCursor['euid'],
                                        institute_id=vCursor['institute_id'],
                                        level_code=vCursor['level_code'],
                                        subject_code=vCursor['subject_code'],
                                        section_code=vCursor['section_code'],
                                        student_id=vStudentDbId,                        
                                        created_date=datetime.today(),
                                        attend_status=global_variables.NO,
                                        attend_status_desc=global_variables.EXAM_ATTENDENCE_STATUS_DESC_NO,                        
                                        sch_start_date=vCursor['sch_start_date'],
                                        sch_end_date=vCursor['sch_end_date'],                        
                                        full_marks=vCursor['full_marks'],
                                        scored_marks=0,
                                        duration=vCursor['duration'],
                                        total_questions=vCursor['total_questions'],
                                        total_attended_questions=0,
                                        updated_date=datetime.today(),   
                                        entry_source=global_variables.EXAM_ATTENDENCE_ENTRY_SOURCE_ADMIN,                                                                                                                                     
                                        )                           
                            vObjReleasedExamAttendance.save() 

                 
        return JsonResponse ({'djStatus':1,})

#-----------------Populate all the Student's Drop Down---------------
def populate_student_drop_down(request):
    if request.method=='POST' :#and request.is_ajax():
        vLevelList,vSectionList=getLevelSectionList(request)        
        return JsonResponse ({'djStatus':1,'djLevelList':vLevelList,'djSectionList':vSectionList,})

#-----------------Populate all the Student's Drop Down---------------
def populate_teacher_drop_down(request):
    if request.method=='POST' and request.is_ajax():
        vSubjectList=getSubjectList(request)        
        return JsonResponse ({'djStatus':1,'djSubjectList':vSubjectList,})



#-----------------Populate all the Student's Drop Down---------------
def populate_student_user_ids(request):
    if request.method=='POST' and request.is_ajax():
        #---find list of students which is belongs to admin's ibstitute
        vLoginId=request.user
        vLoginUserDbId=getUserDbId(vLoginId)
        vLoginInstDbId=getInstituteDbId(vLoginId)
        
        #---this vUserIdList contains all those teachers and students of admin's instiutute        
        vUserIdList=Institute_User.objects.filter(institute_id__exact=vLoginInstDbId,).exclude(user_id__exact=vLoginUserDbId).values_list('user_id', flat=True).distinct()                         
        
        #--this vStudentUserIdList contains only students db_id; now fetch all details from USER table
        vStudentUserIdList=User_Extra_Info.objects.filter(user_id__in=vUserIdList,status__iexact='Active').exclude(type__in=['Teacher','Administrator','TEACHER','ADMINISTRATOR','teacher','administrator']).values_list('user_id', flat=True).distinct()                         
        
        #--Student details list from User Table
        vQsStudentList=User.objects.filter(id__in=vStudentUserIdList).values('id','username')
        vStudentList=list(vQsStudentList) 
        #-----------------------------
        
        # print("BP.....start")   
        # print(vUserIdList)
        # print(vStudentUserIdList)
        # print(vStudentList)        
        # print("BP.....end")   
        

           
        return JsonResponse ({'djStatus':1,'djStudentList':vStudentList,})


#-----------------Populate all the Student's Drop Down---------------
def populate_teacher_user_ids(request):
    if request.method=='POST' :#and request.is_ajax():
        #---find list of students which is belongs to admin's ibstitute
        vLoginId=request.user
        vLoginUserDbId=getUserDbId(vLoginId)
        vLoginInstDbId=getInstituteDbId(vLoginId)
        
        #---this vUserIdList contains all those teachers and students of admin's instiutute        
        vUserIdList=Institute_User.objects.filter(institute_id__exact=vLoginInstDbId,).exclude(user_id__exact=vLoginUserDbId).values_list('user_id', flat=True).distinct()                         
        
        #--this vStudentUserIdList contains only students db_id; now fetch all details from USER table
        vTeacherUserIdList=User_Extra_Info.objects.filter(user_id__in=vUserIdList).exclude(type__in=['Student','Administrator','STUDENT','ADMINISTRATOR','student','administrator']).values_list('user_id', flat=True).distinct()                         
        
        #--Student details list from User Table
        vQsTeacherList=User.objects.filter(id__in=vTeacherUserIdList).values('id','username')
        vTeacherList=list(vQsTeacherList) 
        #-----------------------------
        
        # print("BP.....start")   
        # print(vUserIdList)
        # print(vStudentUserIdList)
        # print(vStudentList)        
        # print("BP.....end")   
        

           
        return JsonResponse ({'djStatus':1,'djTeacherList':vTeacherList,})



#-----------------Search Student---------------
def search_student(request):
    if request.method=='POST' and request.is_ajax():
        vStr=request.POST.get('hSearchString') 
        vUserCount=User.objects.filter(username__icontains=vStr).count() 
        #print("===>",vUserCount)
        vUserDataList=None
        if vUserCount==1:
            vQsUserData=User.objects.values('id','username','first_name','last_name','email','user_extra_info__contact1','user_extra_info__contact2','user_extra_info__profile_pic_path','user_extra_info__status' ).filter(username__icontains=vStr)
            #-----we can call columns of "user_extra_info" becasue it is linked with user by ONE TO ONE relation
            vUserDataList=list(vQsUserData) 
            vStudentDbId=vUserDataList[0]['id']

            #======Get Level & List========[This will not give correct result]===
            # #---get student's level & section list        
            # vStudentLevel=StudentDepartment.objects.filter(user_id__exact=vStudentDbId,).values_list('level_id', flat=True).distinct()                         
            # vStudentSection=StudentDepartment.objects.filter(user_id__exact=vStudentDbId,).values_list('section_id', flat=True).distinct()                         
            
            # #----
            # vQsStudentLevel=Ref_Level.objects.filter(code__in=vStudentLevel).values()                       
            # vStudentLevelList=list(vQsStudentLevel) 
            # #----
            # vQsStudentSection=Ref_Section.objects.filter(code__in=vStudentSection).values()                       
            # vStudentSectionList=list(vQsStudentSection) 

            #======Get Level & List======[This will give CORRECT result]===
            vSQL="""
                    select 
                        a.level_id,b.level,a.section_id,c.section 
                    from  
                        student_department a, home_ref_level b, home_ref_section c 
                    where 1=1 
                    and a.level_id=b.code
                    and a.section_id=c.code
                    and a.user_id= """+"'"+str(vStudentDbId)+"'"
            cursor=connection.cursor()
            cursor.execute(vSQL)
            vStudentLevelAndSectionList=cursor.fetchall()  
            connection.close()
            
            #print("BP====>",vStudentLevelAndSectionList)
            

        else:
            pass # when count >1 or count == 0

    return JsonResponse ({'djStatus':1,'djUserDataList':vUserDataList,'djUserCount':vUserCount,'djStudentLevelAndSectionList':vStudentLevelAndSectionList})

#-----------------Search Teacher---------------
def search_teacher(request):
    if request.method=='POST' :#and request.is_ajax():
        vStr=request.POST.get('hSearchString') 
        vUserCount=User.objects.filter(username__icontains=vStr).count() 
        #print("===>",vUserCount)
        vUserDataList=None
        if vUserCount==1:
            vQsUserData=User.objects.values('id','username','first_name','last_name','email','user_extra_info__contact1','user_extra_info__contact2','user_extra_info__profile_pic_path','user_extra_info__status' ).filter(username__icontains=vStr)
            #-----we can call columns of "user_extra_info" becasue it is linked with user by ONE TO ONE relation
            vUserDataList=list(vQsUserData) 
            vTeacherDbId=vUserDataList[0]['id']

            #======Get Level & List========[This will not give correct result]===
            # #---get student's level & section list        
            # vStudentLevel=StudentDepartment.objects.filter(user_id__exact=vStudentDbId,).values_list('level_id', flat=True).distinct()                         
            # vStudentSection=StudentDepartment.objects.filter(user_id__exact=vStudentDbId,).values_list('section_id', flat=True).distinct()                         
            
            # #----
            # vQsStudentLevel=Ref_Level.objects.filter(code__in=vStudentLevel).values()                       
            # vStudentLevelList=list(vQsStudentLevel) 
            # #----
            # vQsStudentSection=Ref_Section.objects.filter(code__in=vStudentSection).values()                       
            # vStudentSectionList=list(vQsStudentSection) 

            #======Get Level & List======[This will give CORRECT result]===
            vSQL="""
                    select 
                        a.subject_id,b.subject
                    from  
                        teacher_department a, home_ref_subject b
                    where 1=1 
                    and a.subject_id=b.code
                    and a.user_id="""+"'"+str(vTeacherDbId)+"'"
            cursor=connection.cursor()
            cursor.execute(vSQL)
            vTeacherSubjectList=cursor.fetchall()  
            connection.close()
            
            #print("BP====>",vStudentLevelAndSectionList)
            

        else:
            pass # when count >1 or count == 0

    return JsonResponse ({'djStatus':1,'djUserDataList':vUserDataList,'djUserCount':vUserCount,'djTeacherSubjectList':vTeacherSubjectList})
    