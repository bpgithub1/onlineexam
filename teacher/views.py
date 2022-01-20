#-----Django
from django.shortcuts import render,HttpResponse, resolve_url
from django.http.response import JsonResponse
from django.db.models import Sum
from django.db import connection

#-----MODELS
from home.models import Ref_Level, Ref_Section,Ref_Subject,Ref_UID
from teacher.models import EXAM_ATTENDENCE, Exam, Question,Question_Marks, Question_Options, Department,EXAM_RELEASED
from student.models import Department as vStudentDepartment
#----VIEWS
from home.views import getInstituteDbId, getUserDbId

#-----Generic USE
from typing import List
import json
import os
import re
from datetime import date, datetime,timedelta

#----COMMON FUNCITONS
from onlineexam.common import getNewPrimaryKey

#----GLOBAL VARIABLE------
import onlineexam.global_variables as gv

#----SETTING
from onlineexam import settings



#-------------------- WIP CODE -------------------------

#-----------------Re-Release Exam---------------
def create_exam_copy(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        #------Values Comming from Client Page-------------
        vLoginId=request.user
        vEUID=request.POST.get('hEUID')        
        #vUserDbId,vInstDbId=get_user_institute_id(request)
        #--------
        vQsUid=Ref_UID.objects.values().filter(table_code__exact='A01')
        vExistingEUID=vQsUid[0]['uid']
        vEUIDNew=getNewPrimaryKey(vExistingEUID) 
        Ref_UID.objects.filter(table_code='A01').update(uid=vEUIDNew)
        #--------
        vQsExam=Exam.objects.values().filter(uid__exact=vEUID)
        vExamList=list(vQsExam)  
        #-------Insert New Valeus in Exam Table  
        vLevelCode=vQsExam[0]['level_code']
        vSubjectCode=vQsExam[0]['subject_code']
        vInstituteDbId=vQsExam[0]['institute_id']
        vUserDbId=vQsExam[0]['user_id']
        vSectionCode=vQsExam[0]['section_code']
        vTypeCode=vQsExam[0]['type_code']
        vTypeDesc=vQsExam[0]['type_desc']
        vObjExam=Exam(uid=vEUIDNew,
                            user_id=vUserDbId,
                            institute_id=vInstituteDbId,
                            level_code=vLevelCode,                            
                            subject_code=vSubjectCode,
                            source_code='CPY',
                            source_desc='COPY EXAM', 
                            source_uid=""+vEUID+"",
                            section_code=vSectionCode,
                            type_code=vTypeCode,
                            type_desc=vTypeDesc,
                            is_released='NO'
                     )
                   
        vObjExam.save()
        vQsExam=Exam.objects.values().filter(uid__exact=vEUIDNew)
        vExamList=list(vQsExam) 
        #----Make entry of Question reference i.e. marks in question_mark table         
        vQsQuestion=Question_Marks.objects.values().filter(euid__exact=vEUID)
        #vQuestionList=list(vQsQuestion)                                                               
        for i in range(len(vQsQuestion)):            
            vObjQuestionOptions=Question_Marks(  
                                quid=vQsQuestion[i]['quid'],
                                euid=vEUIDNew,
                                user_id=vQsQuestion[i]['user_id'],
                                institute_id=vQsQuestion[i]['institute_id'],
                                marks=vQsQuestion[i]['marks'],                                                                                         
                            )                           
            vObjQuestionOptions.save() 
        
        return JsonResponse ({'status':1,'djExamUIDList':vExamList})




#-----------------Re-Release Exam---------------
def re_release_exam(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        #------Values Comming from Client Page-------------
        vLoginId=request.user
        vEUID=request.POST.get('hEUID')  
        vUserLoginId=request.user      
        #vUserDbId,vInstDbId=get_user_institute_id(vUserLoginId)
        #--------
        vQsUid=Ref_UID.objects.values().filter(table_code__exact='A01')
        vExistingEUID=vQsUid[0]['uid']
        vEUIDNew=getNewPrimaryKey(vExistingEUID) 
        Ref_UID.objects.filter(table_code='A01').update(uid=vEUIDNew)
        #--------
        vQsExam=Exam.objects.values().filter(uid__exact=vEUID)
        vExamList=list(vQsExam)  
        #-------Insert New Valeus in Exam Table  
        vLevelCode=vQsExam[0]['level_code']
        vSubjectCode=vQsExam[0]['subject_code']
        vInstituteDbId=vQsExam[0]['institute_id']
        vUserDbId=vQsExam[0]['user_id']
        vSectionCode=vQsExam[0]['section_code']
        vTypeCode=vQsExam[0]['type_code']
        vTypeDesc=vQsExam[0]['type_desc']
        vObjExam=Exam(uid=vEUIDNew,
                            user_id=vUserDbId,
                            institute_id=vInstituteDbId,
                            level_code=vLevelCode,                            
                            subject_code=vSubjectCode,
                            source_code='RER',
                            source_desc='RERELEASE EXAM', 
                            source_uid=""+vEUID+"",
                            section_code=vSectionCode,
                            type_code=vTypeCode,
                            type_desc=vTypeDesc,
                            is_released='NO'
                     )
                   
        vObjExam.save()
        vQsExam=Exam.objects.values().filter(uid__exact=vEUIDNew)
        vExamList=list(vQsExam) 
        #----Make entry of Question reference i.e. marks in question_mark table         
        vQsQuestion=Question_Marks.objects.values().filter(euid__exact=vEUID)
        #vQuestionList=list(vQsQuestion)                                                               
        for i in range(len(vQsQuestion)):            
            vObjQuestionOptions=Question_Marks(  
                                quid=vQsQuestion[i]['quid'],
                                euid=vEUIDNew,
                                user_id=vQsQuestion[i]['user_id'],
                                institute_id=vQsQuestion[i]['institute_id'],
                                marks=vQsQuestion[i]['marks'],                                                                                         
                            )                           
            vObjQuestionOptions.save() 
        
        return JsonResponse ({'status':1,'djExamUIDList':vExamList})

#--------------------delete exam-------------------------
def release_exam(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        #------Values Comming from Client Page-------------
        vUID=request.POST.get('hEUID')  
        vFullMarks=request.POST.get('hFullMarks')  
        vTotalQuestion=request.POST.get('hTotalQuestion') 
        #----
        vLoginUserName=request.user    
        vLoginUserId=getUserDbId(vLoginUserName)
        vLoginUserInstituteId=getInstituteDbId(vLoginUserName)

        #---Update Exam Table----        
        Exam.objects.filter(uid=vUID).update(is_released="YES")        

        #----Get exam details from exam table (Teacher)  
        vQsExam=Exam.objects.values().filter(uid__exact=vUID)
        vLevelCode=vQsExam[0]['level_code']
        vSectionCode=vQsExam[0]['section_code']
        vSubjectCode=vQsExam[0]['subject_code']
        vInstituteDbId=vQsExam[0]['institute_id']
        vUserDbId=vQsExam[0]['user_id']
        vScheduledStartDate=vQsExam[0]['start_date']
        vScheduledEndDate=vQsExam[0]['end_date']
        vDuration=vQsExam[0]['duration']
        
        #---Insert Values in (Teacher) Released Exam Table------
        vObjReleasedExam=EXAM_RELEASED(  
                        euid=vUID,
                        institute_id=vLoginUserInstituteId,
                        level_code=vLevelCode,
                        subject_code=vSubjectCode,
                        section_code=vSectionCode,
                        released_by=vLoginUserId,
                        sch_start_date=vScheduledStartDate,
                        sch_end_date=vScheduledEndDate,
                        full_marks=vFullMarks,
                        duration=vDuration,
                        total_questions=vTotalQuestion,
                        status=gv.EXAM_RELEASED_STATUS_OPEN,
                        status_desc=gv.EXAM_RELEASED_STATUS_OPEN_DESC,                                                                                                                                         
                        )                           
        vObjReleasedExam.save() 
        if vSectionCode=='A01':
            vQsStudentIds=vStudentDepartment.objects.values('user_id').filter(institute_id__exact=vLoginUserInstituteId,level_id__exact=vLevelCode,).distinct()
        else:
            vQsStudentIds=vStudentDepartment.objects.values('user_id').filter(institute_id__exact=vLoginUserInstituteId,level_id__exact=vLevelCode,section_id__exact=vSectionCode) 
        #---Insert Values in (Teacher) Exam Attendence Table------
        vStudentIdList=list(vQsStudentIds) 
        for vCursor in vStudentIdList:            
            vObjReleasedExamAttendance=EXAM_ATTENDENCE(  
                        euid=vUID,
                        institute_id=vLoginUserInstituteId,
                        level_code=vLevelCode,
                        subject_code=vSubjectCode,
                        section_code=vSectionCode,
                        student_id=vCursor['user_id'],                        
                        created_date=datetime.today(),
                        attend_status=gv.NO,
                        attend_status_desc=gv.EXAM_ATTENDENCE_STATUS_DESC_NO,                        
                        sch_start_date=vScheduledStartDate,
                        sch_end_date=vScheduledEndDate,                        
                        full_marks=vFullMarks,
                        scored_marks=0,
                        duration=vDuration,
                        total_questions=vTotalQuestion,
                        total_attended_questions=0,
                        updated_date=datetime.today(),                                                                                                                                        
                        )                           
            vObjReleasedExamAttendance.save() 
            

        return JsonResponse ({'status':1,'djExamUID':vUID})  






#------------Get All Question Data Associated with a particular exam-------    
def get_exam_specific_all_question_data(request):      
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vEUID=request.POST.get('hEUID') 
        cursor=connection.cursor()
        cursor.execute('select a.uid as "quid",a.particulars as "particulars", b.marks as "marks" from teacher_question a ,teacher_question_marks b where a.uid=b.quid and b.euid="'+vEUID+'"')
        result=cursor.fetchall()  
        connection.close()
        #print("BP CHECK ==> ",result)      
        return JsonResponse ({'status':1,'djQuestionDataList':result})  
     

#------------------Delete Question------------------------
def delete_question(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vEUID=request.POST.get('hEUID') 
        vQUID=request.POST.get('hQUID') 
        vExamSourceCode=request.POST.get('hExamSourceCode') 
        vIsReleased=request.POST.get('hIsExamReleased') 
              
        #vQsExam=Exam.objects.values().filter(uid__exact=vEUID)
        #vIsReleased=vQsExam[0]['is_released']
        vStatus=0
        vQuestionCount=Question_Marks.objects.filter(quid__exact=vQUID).count()  
        print("===",vQuestionCount)          
        if(vIsReleased=='NO' and vExamSourceCode=='FRS') or (vIsReleased=='NO' and vExamSourceCode=='CPY' and vQuestionCount==1):
            Question.objects.filter(uid=vQUID).delete()
            Question_Marks.objects.filter(quid=vQUID).delete()
            Question_Options.objects.filter(quid=vQUID).delete()
            vStatus=1
        elif(vIsReleased=='NO' and vExamSourceCode=='CPY' and vQuestionCount>1):
            Question_Marks.objects.filter(euid=vEUID,quid=vQUID).delete()
            vStatus=2
        else:            
            vStatus=0
            

        return JsonResponse ({'status':vStatus,'djQUID':vQUID}) 



#-------Populate Exam Ids --------
def populate_exam(request):  
    if request.method=='POST':# and request.is_ajax(): #removed as it is depricated in django 4.0
        print(">>>BP [TRACK START]>>>")  
        vEUID=request.POST.get('hEUID') 
        vUserLoginId=request.user 
        vUserDbId=getUserDbId(vUserLoginId)
        vInstDbId=getInstituteDbId(vUserLoginId) 
        vListOfAllowedSubject=Department.objects.filter(user_id__exact=vUserDbId).values_list('subject_id', flat=True).distinct()   
        print(">>>BP>>>",vListOfAllowedSubject)     
        vQsExam=Exam.objects.values().filter(institute_id__exact=vInstDbId,subject_code__in=vListOfAllowedSubject).order_by('uid') 
        vExamList=list(vQsExam)                            
        return JsonResponse ({'status':1,'djExamList':vExamList}) 

#--------------------get specific exam id data-------------------------
def get_exam_data(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vUID=request.POST.get('hUID') 
        vQsExam=Exam.objects.values().filter(uid__exact=vUID)
        vExam=list(vQsExam)
        #---find total no of questions and total marks of a specific exam
        vQsExamTotalQuestions=Question_Marks.objects.filter(euid__exact=vUID).count()
        vQsExamFullMarks=Question_Marks.objects.filter(euid__exact=vUID).aggregate(Sum('marks'))
        vTotalQuestions=vQsExamTotalQuestions
        vTotalMarks=vQsExamFullMarks['marks__sum']
        # print("bp===total qs==>",vTotalQuestions)
        # print("bp==total marks===>",vTotalMarks)
        #vExamQsAndMs=list(vQsExamQsAndMs)
    return JsonResponse ({'status':1,'djExam':vExam,'djTotalQuestions':vTotalQuestions,'djTotalMarks':vTotalMarks}) 


#-------Populate Question Ids from given Exam Id--------
def populate_question(request):    
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vEUID=request.POST.get('hEUID') 
        vUserLoginId=request.user 
        #vUserDbId,vInstDbId=get_user_institute_id(vUserLoginId)         
        vQsQuestion=Question_Marks.objects.values().filter(euid__exact=vEUID).order_by('quid') 
        vQuestionList=list(vQsQuestion)                                                       
        return JsonResponse ({'status':1,'djQuestionList':vQuestionList})  
        
#--------------------get specific question  data-------------------------
def get_question_data(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vUserLoginId=request.user 
        vUserDbId=getUserDbId(vUserLoginId)
        vInstDbId=getInstituteDbId(vUserLoginId) 
        vEUID=request.POST.get('hEUID') 
        vQUID=request.POST.get('hQUID') 
        #---
        vQsQuestion=Question.objects.values().filter(uid__exact=vQUID)
        vQuestionData=list(vQsQuestion)
        #---
        vQsQuestionMarks=Question_Marks.objects.values().filter(euid__exact=vEUID,quid__exact=vQUID)
        vQuestionMarksData=list(vQsQuestionMarks)
        #--
        vQsQuestionOptions=Question_Options.objects.values().filter(quid__exact=vQUID)
        vQuestionOptionData=list(vQsQuestionOptions)
        
        #----get count of said questions
        vQuestionCount=Question_Marks.objects.filter(quid__exact=vQUID).count() 
        
    return JsonResponse ({'status':1,'djQuestionData':vQuestionData,'djQuestionMarksData':vQuestionMarksData,'djQuestionOptionData':vQuestionOptionData,'djQuestionCount':vQuestionCount}) 





    
    
    

#----------------SAVE QUESTION DATA------------------#
def save_exam_question(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vEUID=request.POST.get('hEUID')
        vQUID=request.POST.get('hQUID')
        vQType=request.POST.get('hQType')    
        vQText=request.POST.get('hQText')
        vQAns=request.POST.get('hQAns')
        vQAns=vQAns.strip()
        vQMarks=request.POST.get('hQMarks')
        vLevelCode=request.POST.get('hLevelCode')
        vSubjectCode=request.POST.get('hSubjectCode')
        vDeleteImageFlag=request.POST.get('hDeleteImageFlag') 
        #-------Insert Data in Question_TYPE_DESC


        #vOptArray=request.POST.get('hOptArray')
        vOptArray=json.loads(request.POST['hOptArray'], encoding="utf-8") 
        #---Server Side Validation----
        vFlagValidation=0
        if((vQType=="1" or vQType=="2" or vQType=="3" or vQType=="4") and vQText!="" and vQAns!="" and vQMarks!="" and vLevelCode!="" and vSubjectCode!="" and vOptArray!=""):
            vFlagValidation=1
        else:
            vFlagValidation=0
        #------Do special validation when question type 4 is selected: all lower and no leading/trailing space allowed         
        if vQType=="4":
            vQAns=vQAns.lower()
            if re.search(r"\s", vQAns): #--No Space Allowed Inside i.e. only one word
                vFlagValidation=0                
        else:
            pass    
        #-----DB OPERATION----   
        if(vFlagValidation==1):#------Successful Validation-------            
            #-----Get user_id & Institute_id           
            vUserLoginId=request.user 
            vUserDbId=getUserDbId(vUserLoginId)
            vInstDbId=getInstituteDbId(vUserLoginId)
            vQUIDDatePart=vQUID[0:8]         
            if(vQUIDDatePart=="20991231"): #insert                      
                vQsUid=Ref_UID.objects.values().filter(table_code__exact='A02')
                vExistingUID=vQsUid[0]['uid']
                vUIDNew=getNewPrimaryKey(vExistingUID) 
                Ref_UID.objects.filter(table_code='A02').update(uid=vUIDNew)
                vObjQuestion=Question(  
                                uid=vUIDNew,
                                user_id=vUserDbId,
                                institute_id=vInstDbId,                                                        
                                level_code=vLevelCode,
                                subject_code=vSubjectCode,
                                particulars=vQText,
                                type=vQType,
                                answer=vQAns,

                            )
                vQUID=vUIDNew             
                vObjQuestion.save()
                #---save marks separatelly; because marks of an question can be differnet for different exams  
                vObjQuestionMarks=Question_Marks(  
                                euid=vEUID,
                                quid=vUIDNew,
                                user_id=vUserDbId,
                                institute_id=vInstDbId,                                                        
                                marks=vQMarks,
                                subject_id=vSubjectCode,
                            )                           
                vObjQuestionMarks.save()



            else: #Update  
                vObjQData=Question.objects.values().filter(uid__exact=vQUID)
                vExistingQType=vObjQData[0]['type'] 
                vExistingImagePath=vObjQData[0]['image_path'] 
                #print("===  ",vExistingQType)
                if (vExistingQType==2 or vExistingQType==3):
                    Question_Options.objects.filter(quid=vQUID).delete()
                    #print("===  ",vExistingQType)
                else:
                    pass
                #----Update Question Data----                      
                Question.objects.filter(uid=vQUID).update(
                particulars=vQText,
                    type=vQType,
                    answer=vQAns, 
                )
                #----Update Marks Data---- 
                Question_Marks.objects.filter(euid=vEUID, quid=vQUID).update(                    
                    marks=vQMarks, 
                )
            
            if(vQType=="2" or vQType=="3"):
                #---since update is not possible in case of question options henc we have to delete all the records then we have to insert 
                # Delete all options from option table ,
                
                Question_Options.objects.filter(quid=vQUID).delete()
                #----insert all options again ---Work here 
                for i in range(len(vOptArray)):
                    vObjQuestionOptions=Question_Options(  
                                quid=vQUID,
                                user_id=vUserDbId,
                                institute_id=vInstDbId,                                                        
                                tag=vOptArray[i][0],
                                particulars=vOptArray[i][1],
                                is_correct=vOptArray[i][2],
                            )                           
                    vObjQuestionOptions.save() 
                
            #----write logic to save question's option in db 
            # delete all the data from option and insert again
            # first modify screen to insert slno i.e. A, B, C, D
            #    
        
                       
        else: #---when validation failed 
            vFlagValidation=0
    else:
        pass
    return JsonResponse ({'status':vFlagValidation,"djQUID":vQUID})      

#----------------SAVE QUESTION IMAGE------------------#
def save_exam_question_image(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0 
        vImageSrc = request.FILES.get('img_question')                    
        vQUID=request.POST.get('hQUID') 
        vDeleteImageFlag=request.POST.get('hDeleteImageFlag') 
        #print("=======>",vDeleteImageFlag)
        #-----Read Name of existing file---    
        vObjQData=Question.objects.values().filter(uid__exact=vQUID)
        vExistingImageQName=vObjQData[0]['image_path']     
        #print("QUID= ",vQUID,"Existing Image ",vExistingImageQName)  
            
        #----upload new file 
        vObjQuestionImage=Question.objects.get(uid=vQUID) # working fine
        if(vDeleteImageFlag=="1"):
            #----Update Question Image Path to Null---- 
            Question.objects.filter(uid=vQUID).update(image_path="")
            os.remove(os.path.join(settings.MEDIA_ROOT, vExistingImageQName))
        else:            
            vObjQuestionImage.image_path=vImageSrc
            vObjQuestionImage.save() 
            if(vExistingImageQName!=""):
                os.remove(os.path.join(settings.MEDIA_ROOT, vExistingImageQName))        


    return JsonResponse ({'status':1})      



#--------------------Populate Drop Down (All Exams Related)-------------------------
def populate_exam_drop_down(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vUserLoginId=request.user 
        vUserDbId=getUserDbId(vUserLoginId)
        vInstDbId=getInstituteDbId(vUserLoginId)
        vUID=request.POST.get('hUID') 
        vQsLevel=Ref_Level.objects.values().all().order_by('level') 
        vQsSection=Ref_Section.objects.values().all().order_by('section') 
        #-----Select only those subject which is associated with that teacher only
        vListOfAllowedSubject=Department.objects.filter(user_id__exact=vUserDbId).values_list('subject_id', flat=True).distinct()        
        vQsSubject=Ref_Subject.objects.values().filter(code__in=vListOfAllowedSubject).order_by('subject') 
                
        #vQsSubject=Ref_Subject.objects.values().all().order_by('subject') #-- earlier when teacher was able to see all  
        
        #we can also use like below 
        #vLevel=Ref_Level.objects.values().filter(code='A05').order_by('-level')  
        vLevel=list(vQsLevel)
        vSection=list(vQsSection)
        vSubject=list(vQsSubject)
        
        
        if(vUID==""):            
            vQsExam=Exam.objects.values().filter(institute_id__exact=vInstDbId).order_by('uid') 
            vExam=list(vQsExam)
        else:
            vQsExam=Exam.objects.values().filter(uid__icontains=vUID,institute_id__exact=vInstDbId).order_by('uid') 
            vExam=list(vQsExam)
                      
        return JsonResponse ({'status':1,'djLevel':vLevel,'djSection':vSection,'djSubject':vSubject,'djExam':vExam})  





#------------------Delete Exam------------------------
def delete_exam(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        vUID=request.POST.get('hUID') 
        vQsExam=Exam.objects.values().filter(uid__exact=vUID)
        vIsReleased=vQsExam[0]['is_released']
        vTransactionStatus=0
        vStatusDesc=""
        if(vIsReleased=='NO'):
            Exam.objects.filter(uid=vUID).delete()
            Question_Marks.objects.filter(euid=vUID).delete()     
            vTransactionStatus=1
            vStatusDesc="Deleted Successfully"
        else: 
            vTransactionStatus=0
            vStatusDesc="Released Exam Can't Be Deleted !!!"
            print("BP==>",vIsReleased,": Cannot be deleted")

        

    return JsonResponse ({'status':vTransactionStatus,'status_desc':vStatusDesc,'ExamUID':vUID}) 


#--------------------delete exam-------------------------
def save_exam(request):
    if request.method=='POST' :# and request.is_ajax(): #removed as it is depricated in django 4.0
        #------Values Comming from Client Page-------------
        vLoginId=request.user
        vUID=request.POST.get('hUID')        
        vStartDate=request.POST.get('hStartDate')
        vEndDate=request.POST.get('hEndDate')
        vDuration=request.POST.get('hDuration')
        vLevel=request.POST.get('hLevel')
        vSection=request.POST.get('hSection')        
        vSubject=request.POST.get('hSubject')
        vType=request.POST.get('hType')
        vTypeDesc=""
        if(vType=="LS"):
            vTypeDesc="Long Schedule"
        elif(vType=="SS"):
            vTypeDesc="Short Schedule"
        else:
            vTypeDesc="Not Available"

        #print("BP1====>",vStartDate)
        #vStartDate='2021-10-22T10:22'
        #print("BP2====>",vStartDate)
        
      

        #------Values after processing on server-------------    
        # -----Get user_id & Institute_id    
        vUserLoginId=request.user        
        vUserDbId=getUserDbId(vUserLoginId)
        vInstDbId=getInstituteDbId(vUserLoginId)
        vUIDDatePart=vUID[0:8]
        if(vUIDDatePart=="20991231"): #insert            
            vQsUid=Ref_UID.objects.values().filter(table_code__exact='A01')
            vExistingUID=vQsUid[0]['uid']
            vUIDNew=getNewPrimaryKey(vExistingUID) 
            Ref_UID.objects.filter(table_code='A01').update(uid=vUIDNew)
            vObjExam=Exam(  uid=vUIDNew,
                            user_id=vUserDbId,
                            institute_id=vInstDbId,
                            start_date=vStartDate,
                            end_date=vEndDate,
                            is_released='NO',
                            duration=vDuration,
                            level_code=vLevel,
                            section_code=vSection,
                            subject_code=vSubject,
                            source_code='FRS',
                            source_desc='FRESH EXAM',
                            type_code=vType,
                            type_desc=vTypeDesc,
                         )
            vUID=vUIDNew             
            vObjExam.save()
                        
        else: #Update 
            #---if exam has questions then you cannot chnage the question levels and subject        
            vTotalQuestions=Question_Marks.objects.filter(euid__exact=vUID).count()
            if(vTotalQuestions>0):
                Exam.objects.filter(uid=vUID).update(
                start_date=vStartDate,
                end_date=vEndDate,
                duration=vDuration,                
                section_code=vSection,                
                )   
            else:                        
                Exam.objects.filter(uid=vUID).update(
                start_date=vStartDate,
                end_date=vEndDate,
                duration=vDuration,
                level_code=vLevel,
                section_code=vSection,
                subject_code=vSubject, 
                )


        return JsonResponse ({'status':1,'ExamUID':vUID})  





