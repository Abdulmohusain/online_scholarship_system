from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_student/', views.manage_student, name='manage_student'),
    path('approve_application/', views.approve_application, name='approve_application'),
    path('generate_reports/', views.generate_reports, name='generate_reports'),
]