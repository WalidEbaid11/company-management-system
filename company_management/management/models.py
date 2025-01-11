from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Company(models.Model):
    name = models.CharField(max_length=255)

    @property
    def department_count(self):
        return self.departments.count()

    @property
    def employee_count(self):
        return sum(dept.employee_count for dept in self.departments.all())

    @property
    def project_count(self):
        return sum(dept.project_count for dept in self.departments.all())

class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    @property
    def employee_count(self):
        return self.employees.count()

    @property
    def project_count(self):
        return self.projects.count()

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            return (timezone.now().date() - self.hired_on).days
        return None

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee, related_name='projects')
    
class PerformanceReview(models.Model):
    REVIEW_STAGES = [
        ('Pending Review', 'Pending Review'),
        ('Review Scheduled', 'Review Scheduled'),
        ('Feedback Provided', 'Feedback Provided'),
        ('Under Approval', 'Under Approval'),
        ('Review Approved', 'Review Approved'),
        ('Review Rejected', 'Review Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stage = models.CharField(max_length=20, choices=REVIEW_STAGES, default='Pending Review')
    scheduled_date = models.DateField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def transition_to(self, new_stage):
        allowed_transitions = {
            'Pending Review': ['Review Scheduled'],
            'Review Scheduled': ['Feedback Provided'],
            'Feedback Provided': ['Under Approval'],
            'Under Approval': ['Review Approved', 'Review Rejected'],
            'Review Rejected': ['Feedback Provided'],
        }
        if new_stage in allowed_transitions.get(self.stage, []):
            self.stage = new_stage
            self.save()
        else:
            raise ValueError(f"Invalid transition from {self.stage} to {new_stage}")