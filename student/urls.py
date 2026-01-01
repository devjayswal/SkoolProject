
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path("", views.student_list, name='student-list'),
    path("add/",views.add_student,name="add-student"),
    path('student/<str:slug>/', views.view_student, name='view-student'),
    path('edit/<str:slug>/', views.edit_student, name='edit-student'),
    path('delete/<str:slug>/', views.delete_student, name='delete-student'),
]
