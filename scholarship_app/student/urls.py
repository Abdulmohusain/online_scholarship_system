from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.student_register, name='student_register'),
    path('login/', views.student_login, name='student_login'),
    path('dashboard/', views.student_dashboard, name='student_dashboard'),
    path('profile/', views.student_profile, name='student_profile'),
    path('apply/', views.apply, name='student_apply'),
]