from django import forms
from .models import UserAccount, Intern, Task, TaskAssignment, DepartmentSupervisor, Workload, Concern, Subtask

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'mid_initial','email']

    def __init__(self, *args, **kwargs):
        # Extract the 'partial' keyword argument and remove it before calling the parent constructor
        partial = kwargs.pop('partial', False)
        super(UserAccountForm, self).__init__(*args, **kwargs)

        if partial:
            # Update the fields to mark them as not required for partial updates
            for field_name in self.fields:
                self.fields[field_name].required = False

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ['birthday', 'gender', 'mobile_number', 'school','degree','year_level','internship_type','start_date','end_date','school_coordinator','department_id','nda_file','required_hours']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_due_date', 'task_description', 'task_date_created', 'task_due_date', 'task_estimated_time_to_finish', 'task_points']

class TaskAssignmentForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = ['intern_id', 'task_id', 'task_status', 'date_started']
        
class DepartmentSupervisorForm(forms.ModelForm):
    class Meta:
        model = DepartmentSupervisor
        fields = '__all__'
        
class WorkloadForm(forms.ModelForm):
    class Meta:
        model = Workload
        fields = '__all__'

class ConcernForm(forms.ModelForm):
    class Meta:
        model = Concern
        fields = ["intern_id", "concern_description", "academic_workload", "other_commitments"]
        
class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ('task_id', 'subtask_description')