from django.db import models
from student.models import ScholarshipApplication

class AdminUser(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def __str__(self):
        return self.name


class ScholarshipApproval(models.Model):
    admin = models.ForeignKey(AdminUser, on_delete=models.CASCADE)
    application = models.OneToOneField(ScholarshipApplication, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    decision_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Admin {self.admin.name} - Approval for {self.application.student.matriculation_number}"
