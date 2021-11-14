from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index,name="home"),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('register_institute', views.register_institute, name='register_institute'),
    path('register_individual', views.register_individual, name='register_individual'),
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('change_password', views.change_password, name='change_password'),
    path('profile_details', views.profile_details, name='profile_details'),
    path('profile_details_save', views.profile_details_save, name='profile_details_save'),
    path('profile_extra_details_save', views.profile_extra_details_save, name='profile_extra_details_save'),
    
    path('auto_db_updates', views.auto_db_updates, name='auto_db_updates'),
    
    
    #--Not in use
    path('upload_file',views.upload_file,name="upload_files")

    
    
    
]
