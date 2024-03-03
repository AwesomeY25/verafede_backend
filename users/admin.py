from django.contrib import admin
from .models import UserAccount, Intern, Task, TaskAssignment, Department, DepartmentSupervisor, Workload, Concern

# Register your models here.

@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'timestamp')

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('intern_id', 'department_id', 'gender', 'intern_status', 'birthday', 'mobile_number', 'school', 'year_level', 'degree', 'internship_type', 'school_coordinator', 'start_date', 'end_date', 'min_workload_threshold', 'max_workload_threshold', 'intern_head_status', 'nda_file')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('task_id','task_name','task_due_date')
    
@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task_assignment_id', 'intern_id', 'task_id', 'task_status', 'date_started', 'file_submission')
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_id','department_name')

@admin.register(DepartmentSupervisor)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department_id','user_id')
    
@admin.register(Workload)
class WorkloadAdmin(admin.ModelAdmin):
    list_display=('workload_id','intern_id','week_date','workload_points','workload_tag')
    
@admin.register(Concern)
class ConcernAdmin(admin.ModelAdmin):
    list_display = ('concern_id', 'intern_id', 'date_filed')