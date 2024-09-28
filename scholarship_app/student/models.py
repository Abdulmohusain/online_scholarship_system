from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    PROGRAMME_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    disability_status = models.BooleanField(default=False)
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    address = models.TextField()
    institution_name = models.CharField(max_length=100)
    matriculation_number = models.CharField(max_length=20, unique=True)
    course_of_study = models.CharField(max_length=100)
    programme = models.CharField(max_length=2, choices=PROGRAMME_CHOICES)
    academic_level = models.CharField(max_length=20)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    year_of_graduation = models.IntegerField()

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.matriculation_number}"


class ScholarshipApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    app_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    date_applied = models.DateField(auto_now_add=True)
    decision_date = models.DateField(null=True, blank=True)
    award_letter = models.TextField(blank=True)

    def __str__(self):
        return f"Application {self.app_id} - {self.student.matriculation_number}"

