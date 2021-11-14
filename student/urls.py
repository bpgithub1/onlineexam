from django.urls import path
from student import views

urlpatterns = [
    path('get_available_exams', views.get_available_exams, name='get_available_exams'),
          
]