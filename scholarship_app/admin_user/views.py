from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Student, ScholarshipApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Check if the user is an admin
def admin_check(user):
    return user.is_superuser

# View for admin login
def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid email or password, or you are not an admin.")
    return render(request, 'admin_user/login.html')


# View for admin dashboard (requires login as admin)
@user_passes_test(admin_check, login_url='admin_login')
def admin_dashboard(request):
    student_count = Student.objects.count()
    application_count = ScholarshipApplication.objects.count()

    context = {
        'student_count': student_count,
        'application_count': application_count,
    }
    return render(request, 'admin_user/dashboard.html', context)


# View to manage students (requires login as admin)
@user_passes_test(admin_check, login_url='admin_login')
def manage_student(request):
    students = Student.objects.all()
    
    context = {
        'students': students,
    }
    return render(request, 'admin_user/manage_students.html', context)


# View to approve or reject scholarship applications (requires login as admin)
@user_passes_test(admin_check, login_url='admin_login')
def approve_application(request):
    applications = ScholarshipApplication.objects.all()

    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        action = request.POST.get('action')

        application = ScholarshipApplication.objects.get(id=application_id)
        
        if action == 'approve':
            application.status = 'Approved'
            messages.success(request, "Application approved successfully.")
        elif action == 'reject':
            application.status = 'Rejected'
            messages.error(request, "Application rejected.")
        
        application.save()

    context = {
        'applications': applications,
    }
    return render(request, 'admin_user/approve_application.html', context)


# View to generate reports (requires login as admin)
@user_passes_test(admin_check, login_url='admin_login')
def generate_reports(request):
    students = Student.objects.all()
    applications = ScholarshipApplication.objects.all()

    context = {
        'students': students,
        'applications': applications,
    }
    return render(request, 'admin_user/reports.html', context)


# View for logging out the admin
def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('admin_login')
