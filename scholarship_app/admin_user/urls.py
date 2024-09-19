from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-student/', views.manage_student, name='admin_manage_student'),
]