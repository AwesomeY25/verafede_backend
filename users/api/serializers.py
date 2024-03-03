from django.core.serializers import serialize
from django.http import JsonResponse
from users.forms import UserAccountForm, InternForm, TaskForm, TaskAssignmentForm, DepartmentSupervisorForm, WorkloadForm, ConcernForm
from ..models import UserAccount, Intern, Task, TaskAssignment, DepartmentSupervisor, Workload, Concern

# Serializer for UserAccountForm
def user_account_form_serializer(form_data):
    form = UserAccountForm(form_data)
    if form.is_valid():
        user_account_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for InternForm
def intern_form_serializer(form_data):
    form = InternForm(form_data)
    if form.is_valid():
        intern_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for TaskForm
def task_form_serializer(form_data):
    form = TaskForm(form_data)
    if form.is_valid():
        task_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for TaskAssignmentForm
def task_assignment_form_serializer(form_data):
    form = TaskAssignmentForm(form_data)
    if form.is_valid():
        task_assignment_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for DepartmentSupervisorForm
def department_supervisor_form_serializer(form_data):
    form = DepartmentSupervisorForm(form_data)
    if form.is_valid():
        department_supervisor_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for WorkloadForm
def workload_form_serializer(form_data):
    form = WorkloadForm(form_data)
    if form.is_valid():
        workload_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)

# Serializer for ConcernForm
def concern_form_serializer(form_data):
    form = ConcernForm(form_data)
    if form.is_valid():
        concern_instance = form.save(commit=False)
        # Perform any additional processing if needed
        return JsonResponse({'data': form.cleaned_data})
    else:
        return JsonResponse({'error': form.errors}, status=400)
