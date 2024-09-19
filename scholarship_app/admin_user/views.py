from django.shortcuts import render
from django.http import HttpResponse

def admin_login(request):
    return HttpResponse('ADMIN LOGIN')

def admin_dashboard(request):
    return HttpResponse('ADMIN DASHBOARD')

def manage_student(request):
    return HttpResponse('MANAGE STUDENT')


