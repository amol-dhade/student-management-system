from django.urls import path 
from . import views 

urlpatterns = [
    path('student/form/', views.stu_view, name='student_form_url'),
    path('student/list/', views.stu_list, name='student_list_url'),
    path('student/update/<int:pk>/', views.update_student, name='student_update_url'),
    path('student/delete/<int:pk>/', views.delete_student, name='student_delete_url')
]
