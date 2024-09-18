from django.shortcuts import render
from django.http import HttpResponse


def student_register(request):
    return HttpResponse('STUDENT REGISTER')

def student_login(request):
    return HttpResponse('STUDENT LOGIN')

def student_dashboard(request):
    return HttpResponse('STUDENT DASHBOARD')

def student_profile(request):
    return HttpResponse('STUDENT PROFILE')

def apply(request):
    return HttpResponse('APPLY')
