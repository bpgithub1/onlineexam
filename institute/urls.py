from django.urls import path
from institute import views

urlpatterns = [
    #---student related URLs
    path('populate_student_drop_down', views.populate_student_drop_down  , name='populate_student_drop_down'),
    path('populate_student_user_ids', views.populate_student_user_ids  , name='populate_student_user_ids'),
    path('search_student', views.search_student  , name='search_student'),
    path('save_student_data', views.save_student_data  , name='save_student_data'),
    #---teacher related URLs
    path('populate_teacher_drop_down', views.populate_teacher_drop_down  , name='populate_teacher_drop_down'),
    path('populate_teacher_user_ids', views.populate_teacher_user_ids  , name='populate_teacher_user_ids'),
    path('search_teacher', views.search_teacher  , name='search_teacher'),
    path('save_teacher_data', views.save_teacher_data  , name='save_teacher_data'),
    #----Institute related URLs
    path('get_institute_data', views.get_institute_data  , name='get_institute_data'),
    path('save_institute_details', views.save_institute_details  , name='save_institute_details'),
    path('save_institute_details_image', views.save_institute_details_image  , name='save_institute_details_image'),
    
]    