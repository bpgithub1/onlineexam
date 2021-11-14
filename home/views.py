from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from home.models import Institute,Ref_Level,Ref_Section, Ref_Subject,User_Extra_Info,Institute_User,Automated_Script
from teacher.models import EXAM_RELEASED
from home.forms import  RegisterInstituteForm,UserInfoForm,UserExtraInfoForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.db.models.functions import Upper
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from datetime import date, datetime,timedelta
import os
from onlineexam import settings
from onlineexam import global_variables as gv
from django.db import connection

# Create your views here & current working should be here.


#-----The best of this function is to implement stored procedure; but unfortunately SQLite Does not supports stored procedures
#-----hence we have to do the task in this function.
def auto_db_updates(request):
    vStr=request.user
    #--------Insert Script Execution records----
    #script name: AUTO_DB_UPDATES
    #script Desc: Update Required Tables
    vScriptId='' 
    vScriptAction='Script Execution Started & Script Entry Created|'
    vAutoDbUpdates = Automated_Script(
        script_name=gv.SCRIPT_NAME,   
        script_name_desc=gv.SCRIPT_NAME_DESC,    
        script_execution_mode=  gv.SCRIPT_EXECUTION_MODE_MANUAL,
        script_action=vScriptAction,   
        script_execution_date=datetime.today()
    )
    vAutoDbUpdates.save()
    #---Get ScriptId to update script run progress------
    cursor=connection.cursor()
    cursor.execute("select seq as script_id from sqlite_sequence where name='home_automated_script'")
    result=cursor.fetchall()  
    connection.close()
    vScriptId=result[0][0]
    
    #-------Update Exam Status from OPEN to CLOSE------------
    #-------Exam in which current date is greater than Exam End Date then that exam will be CLOSED 
    vQsReleasedExamCount=EXAM_RELEASED.objects.all().filter(sch_end_date__lte=datetime.today()).exclude(is_processed_by_script=gv.YES).count()
    
    EXAM_RELEASED.objects.filter(sch_end_date__lte=datetime.today()).exclude(is_processed_by_script=gv.YES).update(                    
            status=gv.EXAM_RELEASED_STATUS_CLOSE,
            status_desc=gv.EXAM_RELEASED_STATUS_CLOSE_DESC,    
            is_processed_by_script=gv.YES,
            updated_date=datetime.today(),

    ) 
    vScriptAction=vScriptAction+'EXAM_RELEASED Table Updated - Records ('+str(vQsReleasedExamCount)+')|'
    Automated_Script.objects.filter(id=vScriptId).update(                    
        script_action=vScriptAction,               
        script_execution_date=datetime.today()

    )
    
    #----take ExamId|StudentId (L1) data from Attendance ----

    #----take ExamId from Released Exam & Student Id from Institute Users and concatenate as ExamId|StudentId (L2)

    #select b.user_id from home_institute_user a, home_user_extra_info b where b.user_id=a.user_id and b.type='Student'

    #----L3=L2-L1

    #----Insert L3 in Attendance table


     




    

    #print("bp--Update Database ",vQsReleasedExamCount)    
    return JsonResponse ({'djStatus':1,})  


def profile_details(request):
    #-----Retrieve details and return#====
    vStr=request.user
    vQsUserData=User.objects.values('id','username','first_name','last_name','email','user_extra_info__contact1','user_extra_info__contact2','user_extra_info__profile_pic_path','user_extra_info__status','user_extra_info__address','user_extra_info__verification_id','user_extra_info__verification_id_type' ).filter(username__icontains=vStr)
    vUserDataList=list(vQsUserData)             
    #print("bp----------",vUserDataList)    
    return JsonResponse ({'djStatus':1,'djUserDetails':vUserDataList})  

def profile_details_save(request):
    if request.method=='POST' and request.is_ajax():
        vStr=request.user
        vDbId=request.POST.get('hDbId')
        vFirstName=request.POST.get('hNameFirst')
        vLastName=request.POST.get('hNameLast')
        vContact1=request.POST.get('hContact1')
        vContact2=request.POST.get('hContact2')
        vEmailId=request.POST.get('hEmailId')
        vAddress=request.POST.get('hAddress')
        vVerificationIdType=request.POST.get('hVerificationIdType')
        vVerificationId=request.POST.get('hVerificationId')
        
        User.objects.filter(id=vDbId,username=vStr).update(                    
            first_name=vFirstName,
            last_name=vLastName,
            email=vEmailId,                                        
        )                   
    return JsonResponse ({'djStatus':1}) 

def profile_extra_details_save(request):
    if request.method=='POST' and request.is_ajax():
        vStr=request.user
        vDbId=request.POST.get('hDbId')
        vContact1=request.POST.get('hContact1')
        vContact2=request.POST.get('hContact2')
        vAddress=request.POST.get('hAddress')
        vVerificationIdType=request.POST.get('hVerificationIdType')
        vVerificationId=request.POST.get('hVerificationId')  
        vRemarks='Profile Edited'      
        #-----Read Profile Pic----
        vImageSrcNew = request.FILES.get('file_edit_profile_pic')  
        vQsImagePath=User_Extra_Info.objects.values().filter(user_id=vDbId)
        vImagePathExisting=vQsImagePath[0]['profile_pic_path'] 
        User_Extra_Info.objects.filter(user_id=vDbId).update(                    
            contact1=vContact1,
            contact2=vContact2,
            remarks=vRemarks,
            address=vAddress,
            verification_id_type=vVerificationIdType,
            verification_id=vVerificationId,            
            updated_date=datetime.today()
        ) 
        #------save image (if new image is coming then )
        vObjImage=User_Extra_Info.objects.get(user_id=vDbId)                          
        if vImageSrcNew is not None:        
            vObjImage.profile_pic_path=vImageSrcNew
            vObjImage.save()        
            os.remove(os.path.join(settings.MEDIA_ROOT, vImagePathExisting))
                         
    return JsonResponse ({'djStatus':1}) 

#----------------Delete this after some times-----------------------------
# def get_user_institute_id_BKP(request):
#     vUserLoginId=request.user
#     vQsUser=User.objects.values().filter(username__exact=vUserLoginId).values() 
#     vUser=list(vQsUser)
#     vUserDbId=vUser[0]['id']  
#     vQsInstituteUser=Institute_User.objects.values().filter(user_id__exact=vUserDbId).values() 
#     vInstituteUser=list(vQsInstituteUser)
#     vInstituteDbId=vInstituteUser[0]['institute_id']    
#     return vUserDbId,vInstituteDbId  

def change_password(request):      
    #future -- use password validation 
    vPassOld=request.POST.get('id_old_password')
    vPassNew=request.POST.get('id_new_password1')
    vUserLoginId=request.user
    #print("Change Password View is Called (BP)===>",vUserLoginId)
    vObjId=User.objects.filter(username__iexact=vUserLoginId).values() 
    vId=int(vObjId[0]['id'])
    vIsUserAuthenticated = authenticate(username=vUserLoginId, password=vPassOld)
    if request.method=='POST' and request.is_ajax()  and vIsUserAuthenticated is not None: 
        vObjUser=User.objects.get(pk=vId) 
        #vObjUser.set_password(vPassNew) # this is working fine you can use this code as well 
        vObjUser.password=make_password(vPassNew)
        #vObjUser.email='abc@gmail.com' # take is as sample to use in another place
        vObjUser.save() #this save will work as update      
        return JsonResponse ({'status':1})  
        
    else:
        return JsonResponse ({'status':0})                      
        #return redirect("/login_user")

def login_user(request):
    #return render(request,"teacher/index.html",{'djInstitute':"Habile Academia",'djProfile':"Teacher",'djUser':"Suman Prajapati"}) # this is just for testing purpose
    if request.method=='POST':
        vUserInstitute=request.POST.get('id_institute')
        vUserLoginProfile=request.POST.get('id_login_type')
        vUserLoginId=request.POST.get('id_username')
        vUserLoginPassword=request.POST.get('id_password')

        if vUserLoginProfile==None:
            messages.add_message(request, messages.ERROR, 'Select Your Profile ')
            messages.info(request, 'Try Again !!!')

        elif vUserLoginProfile=="Manager":
            vIsManagerAuthenticated=authenticate(username=vUserLoginId, password=vUserLoginPassword) 
            if vIsManagerAuthenticated is not None:
                vUserObj=User.objects.filter(username__iexact=vUserLoginId).values() 
                if vUserObj[0]['is_active']==False:
                    messages.add_message(request, messages.ERROR, 'Your Account is Inactive - Contact Software Center')                    
                elif vUserObj[0]['is_superuser']==False:
                    messages.add_message(request, messages.ERROR, 'Insufficient Priviledges  - Contact Software Center')
                elif vUserObj[0]['is_staff']==False:
                    messages.add_message(request, messages.ERROR, 'Insufficient Priviledges  - Contact Software Center')
                else:        
                    login(request,vIsManagerAuthenticated)
                    vLoggedInFullName=vUserObj[0]['first_name']+" "+vUserObj[0]['last_name']
                    #return render(request,"manager/index.html",{'djLoginId':vUserLoginId,'djFullName':vLoggedInFullName,})
                    fm=PasswordChangeForm(user=request.user)
                    return render(request,"manager/index.html",{'djInstitute':'All Institute','djProfile':vUserLoginProfile,'djUser':vLoggedInFullName,'djForm':fm}) 
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Login Credential for S/W Manager Account')
                messages.info(request, 'Try Again !!!')
        elif vUserLoginProfile=="Student":
            vIsUserAuthenticated=authenticate(username=vUserLoginId, password=vUserLoginPassword)
            if vIsUserAuthenticated is not None:
                vUserObj=User.objects.filter(username__iexact=vUserLoginId).values()                      
                if vUserObj[0]['is_active']==False:
                    messages.add_message(request, messages.ERROR, 'Your Account is Inactive - Contact Software Center')                       
                else:
                    vIsProfileMatched=User_Extra_Info.objects.filter(type__exact=vUserLoginProfile,user_id__exact=vUserObj[0]['id']).count()                    
                    if vIsProfileMatched==0:    
                        messages.add_message(request, messages.ERROR, 'You Have Selected WRONG PROFILE ')
                        messages.info(request, 'Try Again !!!')   
                    else:
                        vLoggedInFullName=vUserObj[0]['first_name']+" "+vUserObj[0]['last_name']
                        vLoggedInInstName="Common Portal"
                        fm=PasswordChangeForm(user=request.user) # for change password                                                             
                        login(request,vIsUserAuthenticated)
                        return render(request,"student/index.html",{'djInstitute':vLoggedInInstName,'djProfile':vUserLoginProfile,'djUser':vLoggedInFullName,'djForm':fm})                             
            else:
                vUserObj=User.objects.filter(username__iexact=vUserLoginId).values()                                 
                if vUserObj[0]['is_active']==False:
                    messages.add_message(request, messages.ERROR, 'Your Account is Inactive - Contact Software Center')                       
                else:
                    messages.add_message(request, messages.ERROR, 'WRONG CREDNETIALS PROVIDED ')
                    messages.info(request, 'Try Again !!!')      
            messages.add_message(request, messages.ERROR, 'Select Your Institute ')
            messages.info(request, 'Try Again !!!')
        else: # if profile is selected other than the S/W Manager & Student i.e. for TEACHER & ADMINISTRATOR 
            if vUserInstitute==None:
                messages.add_message(request, messages.ERROR, 'Select Your Institute ')
                messages.info(request, 'Try Again !!!')
            else:
                vIsUserAuthenticated=authenticate(username=vUserLoginId, password=vUserLoginPassword)
                if vIsUserAuthenticated is not None:
                    vUserObj=User.objects.filter(username__iexact=vUserLoginId).values()                      
                    if vUserObj[0]['is_active']==False:
                        messages.add_message(request, messages.ERROR, 'Your Account is Inactive - Contact Software Center')                       
                    else:
                        vIsProfileMatched=User_Extra_Info.objects.filter(type__exact=vUserLoginProfile,user_id__exact=vUserObj[0]['id']).count()
                        
                        if vIsProfileMatched==0:    
                            messages.add_message(request, messages.ERROR, 'You Have Selected WRONG PROFILE ')
                            messages.info(request, 'Try Again !!!')
                        else:                            
                            vIsInstituteMatched=Institute_User.objects.filter(institute_id__exact=vUserInstitute,user_id__exact=vUserObj[0]['id']).count()
                            if vIsInstituteMatched==0: 
                                messages.add_message(request, messages.ERROR, 'You Have Selected WRONG INSTITUTE ')
                                messages.info(request, 'Try Again !!!')
                            else:
                                login(request,vIsUserAuthenticated)
                                #print("<<<<<<==============BP(Marker)================>>>>>>>") 
                                # print(  "\n Institute Id Entered:",vUserInstitute,
                                #         "\n User Login Profile:",vUserLoginProfile,
                                #         "\n User Login Id:",vUserLoginId,
                                #         "\n User Login Password:",vUserLoginPassword,
                                #         "\n User Institute Matched:",vIsInstituteAndProfileMatched,
                                #         "\n User Login Internal Id:",vUserObj[0]['id'],
                                #         "\n Is User Authenticated:",vIsUserAuthenticated,
                                #         "\n Is User Active:",vUserObj[0]['is_active'],) 

                                vLoggedInFullName=vUserObj[0]['first_name']+" "+vUserObj[0]['last_name']
                                vInstituteName=Institute.objects.filter(id__exact=vUserInstitute).values()   
                                vLoggedInInstName=vInstituteName[0]['institute_name']
                                fm=PasswordChangeForm(user=request.user) # for change password                             
                                if vUserLoginProfile=="Administrator":
                                    return render(request,"institute/index.html",{'djInstitute':vLoggedInInstName,'djProfile':vUserLoginProfile,'djUser':vLoggedInFullName,'djForm':fm}) 

                                elif vUserLoginProfile=="Teacher":
                                    return render(request,"teacher/index.html",{'djInstitute':vLoggedInInstName,'djProfile':vUserLoginProfile,'djUser':vLoggedInFullName,'djForm':fm}) 
                                
                                #----This code is not used 
                                elif vUserLoginProfile=="Student": 
                                    return render(request,"student/index.html",{'djInstitute':vLoggedInInstName,'djProfile':vUserLoginProfile,'djUser':vLoggedInFullName,'djForm':fm})                             
                                else:
                                    pass 
                else:
                    vUserObj=User.objects.filter(username__iexact=vUserLoginId).values() 
                    print(vUserObj)   
                    print(vUserObj[0]['is_active'])                  
                    if vUserObj[0]['is_active']==False:
                        messages.add_message(request, messages.ERROR, 'Your Account is Inactive - Contact Software Center')                       
                    else:
                        messages.add_message(request, messages.ERROR, 'WRONG CREDNETIALS PROVIDED ')
                    messages.info(request, 'Try Again !!!')            
    else:
        pass    
    vUserInstitute=Institute.objects.values('institute_name','id').filter(institute_status__exact='Active')  
    return render(request,'home/login.html',{'djFormInstituteList':vUserInstitute})
 


def register_individual(request):
    if request.method=='POST':
        user_info_form=UserInfoForm(data=request.POST)
        user_extra_info_form=UserExtraInfoForm(request.POST,request.FILES)
        vInstitute=request.POST.get('id_institute')
        vProfile=request.POST.get('id_type')
        vIdCardType=request.POST.get('id_verification_id_type')  
            
        # print(user_extra_info_form.errors) 
        # print(user_info_form.errors) 

        if(vInstitute==None):
            vInstitute=0
       
        if user_info_form.is_valid() and user_extra_info_form.is_valid():                   
            vUserConfPassword=user_info_form.cleaned_data['confirm_password'] 
            vUserPassword=user_info_form.cleaned_data['password'] 
            vUserEmail=user_info_form.cleaned_data['email'] 
            vUserFirstName=user_info_form.cleaned_data['first_name'] 
            vUserLastName=user_info_form.cleaned_data['last_name'] 
            #--------------------------------------------------------
             
            vUserContact1=user_extra_info_form.cleaned_data['contact1']
            vUserContact2=user_extra_info_form.cleaned_data['contact2']
            vUserVerificationId=user_extra_info_form.cleaned_data['verification_id']
            vUserAddress=user_extra_info_form.cleaned_data['address']
              
            vProfilePath=user_extra_info_form.cleaned_data['profile_pic_path']
            qExistingUser=User.objects.filter(username__icontains=vUserEmail).count()
            vIsActive=0 
            
            if qExistingUser !=0:                    
                return JsonResponse ({"status":"2"})   #User Exists Response
                
            else:
                # if vProfile=='Administrator':
                #     vIsActive=0                                      
                user_info = User.objects.create_user(username=vUserEmail, 
                                                     password=vUserPassword,
                                                     email=vUserEmail,
                                                     first_name=vUserFirstName,
                                                     last_name=vUserLastName,
                                                     is_active=vIsActive)
                user_extra_info=User_Extra_Info( user=user_info,
                                                contact1=vUserContact1,
                                                contact2=vUserContact2,
                                                verification_id_type=vIdCardType,
                                                verification_id=vUserVerificationId,
                                                address=vUserAddress,
                                                type=vProfile,
                                                profile_pic_path=vProfilePath,
                                                )
                user_extra_info.save()
                
                #=====get db id
                vUserDbId=getUserDbId(vUserEmail)                                   
                if vProfile !='Student' and vInstitute!=0:
                    user_institute_info = Institute_User(user_id=vUserDbId,institute_id=vInstitute,joining_date=datetime.today())
                    user_institute_info.save()
                login(request,user_info)
                
                return JsonResponse ({"status":"1"})                                            
    else:        
        user_info_form=UserInfoForm(request.GET)
        user_extra_info_form=UserExtraInfoForm(request.GET)    
    vInst=Institute.objects.values('institute_name','id').filter(institute_status__exact='Active')        
    return render(request,'home/register_individual.html',{'djFormInstList':vInst,'djFormUserInfo':user_info_form,'djFormUserExtraInfo':user_extra_info_form})

def register_institute(request):    
    if request.method=='POST':        
        fm=RegisterInstituteForm(request.POST,request.FILES)  
        #print("BP-Reg-Inst===>",request.FILES)
        if fm.is_valid():
            
            vInstituteName=fm.cleaned_data['institute_name']    
            vInstituteOwner=fm.cleaned_data['institute_owner']
            vInstituteContact1=fm.cleaned_data['institute_contact1']
            vInstituteContact2=fm.cleaned_data['institute_contact2']
            vInstituteEmail=fm.cleaned_data['institute_email']
            vInstituteCountry=fm.cleaned_data['institute_country']    
            vInstituteState=fm.cleaned_data['institute_state']
            vInstituteCity=fm.cleaned_data['institute_city']
            vInstituteAddress=fm.cleaned_data['institute_address']
            vInstitutePinCode=fm.cleaned_data['institute_pin_code']
            vLogoPath=fm.cleaned_data['institute_logo_path']
            reg=Institute(  institute_name=vInstituteName,
                            institute_owner=vInstituteOwner,
                            institute_contact1=vInstituteContact1,
                            institute_contact2=vInstituteContact2,
                            institute_email=vInstituteEmail,
                            institute_country=vInstituteCountry,
                            institute_state=vInstituteState,
                            institute_city=vInstituteCity,
                            institute_address=vInstituteAddress,
                            institute_pin_code=vInstitutePinCode,
                            institute_logo_path=vLogoPath
                         )
            qInst=Institute.objects.filter(institute_name__iexact=vInstituteName).count()                        
            if (qInst==0):
                
                reg.save()
                
                messages.add_message(request, messages.SUCCESS, 'Your Account has been created !!!')
                messages.info(request, 'But it is IN-ACTIVE (To Activate Please Contact S/W Center) !!!')
                return render(request,'home/register_institute_success.html',{'djForm':fm,'djMessageTag':'Institute Registered Successfully !!!'})
            else:
                messages.add_message(request, messages.ERROR, 'Account Already Exists !!!')
                messages.info(request, 'Try Again !!!')

    else:
        fm=RegisterInstituteForm(request.GET)  
    return render(request,'home/register_institute.html',{'djForm':fm})







def index(request):
    context= {
        'var1':"variable1 from views",
        'var2':"variable2 from views",
    }
    # if request.user.is_anonymous:
    #     return redirect("/login")

    return render(request,'home/index.html',context)
   

def about(request):
    return render(request,'home/x_layout.html')
    #return render(request,'home/about.html')
    

def contact(request):
    return render(request,'home/contact.html')
    



        
# #this function is not is used just kept for ref. you can delete it any time
# def x_change_password(request):    
#     if request.user.is_authenticated:
#         vLoggedInUser=User.objects.filter(username__exact=request.user).values()
#         vLoggedInFullName=vLoggedInUser[0]['first_name']+" "+vLoggedInUser[0]['last_name']
#         vLoggedInInternalId=vLoggedInUser[0]['id']
#         vInstituteUser=Institute_User.objects.filter(user_id__exact=vLoggedInInternalId).values()
#         vProfile=vInstituteUser[0]['type']
#         vInstituteId=vInstituteUser[0]['institute_id']
#         vInstitute=Institute.objects.filter(id__exact=vInstituteId).values()
#         vInstituteName=vInstitute[0]['institute_name']
#         if request.method=='POST':
#             fm=PasswordChangeForm(user=request.user,data=request.POST)
#             if fm.is_valid():
#                 fm.save()
#                 messages.add_message(request, messages.Success, 'Password Changed Successfully !!! ')
#                 return redirect("/")
#         else:           
#             fm=PasswordChangeForm(user=request.user)
#         return render(request,'home/change_password.html',{'djInstitute':vInstituteName,'djProfile':vProfile,'djUser':vLoggedInFullName,'djForm':fm})
#     else:
#         return redirect("/login_user")   

def upload_file(request):
    pass

def logout_user(request):
    logout(request)
    #return render(request,"index.html")
    return redirect("/")

#--------Home View Common functions==============  
#--------------------Get Level & Section List-------------------------
def getLevelSectionList(request):
    vQsLevel=Ref_Level.objects.values().all().order_by('level') 
    vQsSection=Ref_Section.objects.values().all().order_by('section')
    vLevel=list(vQsLevel)
    vSection=list(vQsSection)
    return vLevel, vSection

#--------------------Get Level & Section List-------------------------
def getSubjectList(request):
    vQsSubject=Ref_Subject.objects.values().all().order_by('subject') 
    vSubject=list(vQsSubject)
    return vSubject

#------------CHECK THIS FUCNTION JUST EDITED---------
def getInstituteDbId(pUserId):
    vUserDbId=getUserDbId(pUserId)     
    vQsInstituteUser=Institute_User.objects.values().filter(user_id__exact=vUserDbId) 
    vInstituteUserList=list(vQsInstituteUser)
    if(len(vInstituteUserList)>1):
        return vInstituteUserList
    else:
        vInstituteDbId=vInstituteUserList[0]['institute_id']    
        return vInstituteDbId

def getUserDbId(pUserId):
    vUserId=pUserId
    vQsUser=User.objects.values().filter(username__iexact=vUserId)
    vUser=list(vQsUser)
    vUserDbId=vUser[0]['id']            
    return vUserDbId