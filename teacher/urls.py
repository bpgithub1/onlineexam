from teacher import views 
from django.urls import path

urlpatterns = [
    path('populate_exam_drop_down', views.populate_exam_drop_down, name='populate_exam_drop_down'),
    path('save_exam', views.save_exam, name='save_exam'),
    path('delete_exam', views.delete_exam, name='delete_exam'),
    path('get_exam_data', views.get_exam_data , name='get_exam_data'),
    path('save_exam_question', views.save_exam_question , name='save_exam_question'),
    path('save_exam_question_image', views.save_exam_question_image , name='save_exam_question_image'),
    path('populate_question', views.populate_question , name='populate_question'),
    path('populate_exam', views.populate_exam , name='populate_exam'),
    path('get_question_data', views.get_question_data , name='get_question_data'),
    path('delete_question', views.delete_question , name='delete_question'),
    path('get_exam_specific_all_question_data', views.get_exam_specific_all_question_data , name='get_exam_specific_all_question_data'),
    path('release_exam', views.release_exam , name='release_exam'),
    path('re_release_exam', views.re_release_exam , name='re_release_exam'),
    path('create_exam_copy', views.create_exam_copy , name='create_exam_copy'),    
    
]