# from django.urls import path
# from . import views
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CompanyViewSet, DepartmentViewSet, EmployeeViewSet, ProjectViewSet, PerformanceReviewViewSet

# router = DefaultRouter()
# router.register('companies', CompanyViewSet)
# router.register('departments', DepartmentViewSet)
# router.register('employees', EmployeeViewSet)
# router.register('projects', ProjectViewSet)
# router.register('performance-reviews', PerformanceReviewViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('', views.home, name='home'),
#     path('companies/', views.companies, name='companies'),
#     path('companies/<int:id>/', views.company_detail, name='company_detail'),
#     path('departments/', views.departments, name='departments'),
#     path('departments/<int:id>/', views.department_detail, name='department_detail'),
#     path('employees/', views.employees, name='employees'),
#     path('employees/<int:id>/', views.employee_detail, name='employee_detail'),
#     path('projects/', views.projects, name='projects'),
#     path('projects/<int:id>/', views.project_detail, name='project_detail'),
# ]
from django.urls import path
from . import views

urlpatterns = [
   
    # الصفحة الرئيسية
    path('', views.home, name='home'),

    # مسارات الشركات
    path('companies/', views.companies, name='companies'),
    path('companies/<int:id>/', views.company_detail, name='company_detail'),

    # مسارات الأقسام
    path('departments/', views.departments, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='department_detail'),

    # مسارات الموظفين
    path('employees/', views.employees, name='employees'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),

    # مسارات المشاريع
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
]