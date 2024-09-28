from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, ScholarshipApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# View for the home page
def home(request):
    return render(request, 'student/home.html')


# View for student registration
def student_register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        disability_status = request.POST.get('disability_status')
        state = request.POST.get('state')
        lga = request.POST.get('lga')
        address = request.POST.get('address')
        institution_name = request.POST.get('institution_name')
        matriculation_number = request.POST.get('matriculation_number')
        course_of_study = request.POST.get('course_of_study')
        programme = request.POST.get('programme')
        academic_level = request.POST.get('academic_level')
        cgpa = request.POST.get('cgpa')
        year_of_graduation = request.POST.get('year_of_graduation')
        
        # Create the student record in the database
        student = Student.objects.create(
            fname=fname, lname=lname, surname=surname, email=email, phone_number=phone_number,
            gender=gender, date_of_birth=dob, disability_status=disability_status, state=state, 
            lga=lga, address=address, institution_name=institution_name, matriculation_number=matriculation_number, 
            course_of_study=course_of_study, programme=programme, academic_level=academic_level, 
            cgpa=cgpa, year_of_graduation=year_of_graduation
        )
        student.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('student_login')
    return render(request, 'student/register.html')


# View for student login
def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid email or password")
    return render(request, 'student/login.html')


# View for student dashboard (requires login)
@login_required(login_url='student_login')
def student_dashboard(request):
    # Fetch the student details and applications for this student
    student = Student.objects.get(email=request.user.email)
    applications = ScholarshipApplication.objects.filter(student=student)
    
    context = {
        'student': student,
        'applications': applications,
    }
    return render(request, 'student/dashboard.html', context)


# View for student profile
@login_required(login_url='student_login')
def student_profile(request):
    student = Student.objects.get(email=request.user.email)
    
    if request.method == 'POST':
        # Update student profile
        student.fname = request.POST.get('fname')
        student.surname = request.POST.get('surname')
        student.lname = request.POST.get('lname')
        student.phone_number = request.POST.get('phone_number')
        student.address = request.POST.get('address')
        student.cgpa = request.POST.get('cgpa')
        student.save()
        messages.success(request, "Profile updated successfully")
        return redirect('student_profile')

    context = {
        'student': student,
    }
    return render(request, 'student/profile.html', context)


# View for student to apply for scholarship
@login_required(login_url='student_login')
def apply(request):
    student = Student.objects.get(email=request.user.email)

    if request.method == 'POST':
        # Create a scholarship application
        application = ScholarshipApplication.objects.create(student=student)
        application.save()
        messages.success(request, "Scholarship application submitted successfully")
        return redirect('student_dashboard')

    return render(request, 'student/apply.html')


# View for checking scholarship application status
@login_required(login_url='student_login')
def check_status(request):
    student = Student.objects.get(email=request.user.email)
    applications = ScholarshipApplication.objects.filter(student=student)
    
    context = {
        'applications': applications,
    }
    return render(request, 'student/status.html', context)


# View for logging out the student
def student_logout(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('student_login')
