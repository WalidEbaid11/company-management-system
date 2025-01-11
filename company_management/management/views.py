# from django.shortcuts import render, get_object_or_404
# from .models import Company, Department, Employee, Project
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required, user_passes_test
# from rest_framework import viewsets
# from .models import Company, Department, Employee, Project, PerformanceReview
# from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, ProjectSerializer, PerformanceReviewSerializer
# from django.shortcuts import render

# def home(request):
#     return render(request, 'management/home.html')

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class PerformanceReviewViewSet(viewsets.ModelViewSet):
#     queryset = PerformanceReview.objects.all()
#     serializer_class = PerformanceReviewSerializer
# def is_admin(user):
#     return user.role == 'Admin'

# def is_manager(user):
#     return user.role == 'Manager'

# @login_required
# @user_passes_test(is_admin)
# def admin_dashboard(request):
#     return render(request, 'admin_dashboard.html')

# @login_required
# @user_passes_test(is_manager)
# def manager_dashboard(request):
#     return render(request, 'manager_dashboard.html')

# def home(request):
#     return render(request, 'management/home.html')

# def home(request):
#     return render(request, 'management/home.html')

# def companies(request):
#     companies = Company.objects.all()
#     return render(request, 'management/companies.html', {'companies': companies})

# def company_detail(request, id):
#     company = get_object_or_404(Company, id=id)
#     return render(request, 'management/company_detail.html', {'company': company})

# def departments(request):
#     departments = Department.objects.all()
#     return render(request, 'management/departments.html', {'departments': departments})

# def department_detail(request, id):
#     department = get_object_or_404(Department, id=id)
#     return render(request, 'management/department_detail.html', {'department': department})

# def employees(request):
#     employees = Employee.objects.all()
#     return render(request, 'management/employees.html', {'employees': employees})

# def employee_detail(request, id):
#     employee = get_object_or_404(Employee, id=id)
#     return render(request, 'management/employee_detail.html', {'employee': employee})

# def projects(request):
#     projects = Project.objects.all()
#     return render(request, 'management/projects.html', {'projects': projects})

# def project_detail(request, id):
#     project = get_object_or_404(Project, id=id)
#     return render(request, 'management/project_detail.html', {'project': project})

from django.shortcuts import render, get_object_or_404
from .models import Company, Department, Employee, Project

# الصفحة الرئيسية
def home(request):
    return render(request, 'management/home.html')

# عرض جميع الشركات
def companies(request):
    companies = Company.objects.all()
    return render(request, 'management/companies.html', {'companies': companies})

# تفاصيل شركة معينة
def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    return render(request, 'management/company_detail.html', {'company': company})

# عرض جميع الأقسام
def departments(request):
    departments = Department.objects.all()
    return render(request, 'management/departments.html', {'departments': departments})

# تفاصيل قسم معين
def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(request, 'management/department_detail.html', {'department': department})

# عرض جميع الموظفين
def employees(request):
    employees = Employee.objects.all()
    return render(request, 'management/employees.html', {'employees': employees})

# تفاصيل موظف معين
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'management/employee_detail.html', {'employee': employee})

# عرض جميع المشاريع
def projects(request):
    projects = Project.objects.all()
    return render(request, 'management/projects.html', {'projects': projects})

# تفاصيل مشروع معين
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'management/project_detail.html', {'project': project})