from django.contrib import admin
from .models import User, Company, Department, Employee, Project, PerformanceReview

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('role',)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_count', 'employee_count', 'project_count')
    search_fields = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'employee_count', 'project_count')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'designation', 'hired_on', 'days_employed', 'department', 'company')
    search_fields = ('name', 'email', 'mobile')
    list_filter = ('department', 'company')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'department', 'company')
    search_fields = ('name', 'description')
    list_filter = ('department', 'company')

class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('employee', 'stage', 'scheduled_date', 'approved_by', 'created_at', 'updated_at')
    search_fields = ('employee__name', 'employee__email', 'stage')
    list_filter = ('stage', 'approved_by')

# Register models with custom admin views
admin.site.register(User, UserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(PerformanceReview, PerformanceReviewAdmin)
