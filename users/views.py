from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
import json
from .forms import UserAccountForm, InternForm, TaskForm, TaskAssignmentForm, ConcernForm, WorkloadForm
from django.http import JsonResponse, HttpResponse
from .models import UserAccount, Intern, TaskAssignment, Task, Workload, Concern
import random
import string
import datetime
from django.db import transaction

# USER FUNCTIONS
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        
        if form.is_valid():
            user_instance = form.save(commit=False)  # Do not commit to DB yet
            # Automate username
            if not user_instance.username:
                user_instance.username = f"{user_instance.first_name[:2]}{user_instance.last_name}"

            # Automate password
            if not user_instance.password:
                user_instance.password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

            user_instance.save()  # Now save with automated username and password

            return JsonResponse({'message': 'User created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def get_all_user(request):
    users = UserAccount.objects.all()
    data = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_user(request, id):
    user = get_object_or_404(UserAccount, id=id)
    data = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return JsonResponse(data)

@csrf_exempt
def delete_user(request, id):
    user = get_object_or_404(UserAccount, user_id=id)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_user(request, id):
    user = get_object_or_404(UserAccount, user_id=id)
    if request.method == 'PATCH':
        form = UserAccountForm(request.POST, instance=user, partial=True)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User updated successfully'}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# INTERN FUNCTIONS
@csrf_exempt
def create_intern(request):
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Intern created successfully'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_all_intern(request):
    # Get query parameter for sorting
    sort_by = request.GET.get('sort_by', 'internship_type')  # Default sort by intern_id

    # Check if the sort_by field is valid
    valid_sort_fields = ['gender', 'birthday', 'mobile_number', 'school', 'year_level', 'degree', 'internship_type', 'school_coordinator', 'start_date', 'end_date', 'nda_file']
    if sort_by not in valid_sort_fields:
        return JsonResponse({'error': 'Invalid sort field'}, status=400)
    
    interns = Intern.objects.select_related('user').all()
    interns_data = [
        {
            'intern_id': intern.intern_id,
            'username': intern.user.username,
            'first_name': intern.user.first_name,
            'last_name': intern.user.last_name,
            'mid_initial': intern.user.mid_initial,
            'account_type': intern.user.account_type,
            'email': intern.user.email,
            'gender': intern.gender,
            'intern_status': intern.intern_status,
            'birthday': intern.birthday,
            'mobile_number': intern.mobile_number,
            'school': intern.school,
            'year_level': intern.year_level,
            'degree': intern.degree,
            'internship_type': intern.internship_type,
            'school_coordinator': intern.school_coordinator,
            'start_date': intern.start_date,
            'end_date': intern.end_date,
            'nda_file': intern.nda_file,
            'min_workload_threshold': intern.min_workload_threshold,
            'max_workload_threshold': intern.max_workload_threshold,
            'intern_head_status': intern.intern_head_status,
        }
        for intern in interns
    ]
    return JsonResponse(interns_data, safe=False)

@csrf_exempt
def get_intern(request, intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    data = {
            'intern_id': intern.intern_id,
            'username': intern.user.username,
            'first_name': intern.user.first_name,
            'last_name': intern.user.last_name,
            'mid_initial': intern.user.mid_initial,
            'account_type': intern.user.account_type,
            'email': intern.user.email,
            'gender': intern.gender,
            'intern_status': intern.intern_status,
            'birthday': intern.birthday,
            'mobile_number': intern.mobile_number,
            'school': intern.school,
            'year_level': intern.year_level,
            'degree': intern.degree,
            'internship_type': intern.internship_type,
            'school_coordinator': intern.school_coordinator,
            'start_date': intern.start_date,
            'end_date': intern.end_date,
            'nda_file': intern.nda_file,
            'min_workload_threshold': intern.min_workload_threshold,
            'max_workload_threshold': intern.max_workload_threshold,
            'intern_head_status': intern.intern_head_status,
    }
    return JsonResponse(data)

@csrf_exempt
def delete_intern(request, intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    if request.method == 'DELETE':
        intern.delete()
        return JsonResponse({'message': 'Intern deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_intern(request, intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    if request.method == 'PATCH':
        form = InternForm(request.POST, instance=intern, partial=True)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Intern updated successfully'}, status=200)
        else:
            return JsonResponse(form.errors, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# CREATE INTERN AND USER PROFILE FROM INFO FORM
@csrf_exempt
def create_user_and_intern(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_form = UserAccountForm(data)
            intern_form = InternForm(data)
            
            if user_form.is_valid() and intern_form.is_valid():
                with transaction.atomic():
                    user_instance = user_form.save(commit=False)
                    intern_instance = intern_form.save(commit=False)
                    
                    # Automate username and password if needed
                    if not user_instance.username:
                        user_instance.username = f"{user_instance.first_name[:2]}{user_instance.last_name}"

                    if not user_instance.password:
                        user_instance.password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

                    user_instance.save()

                    # Assuming you have a foreign key relationship between UserAccount and Intern
                    intern_instance.user = user_instance
                    intern_instance.save()
                
                return JsonResponse({'message': 'User and Intern created successfully'}, status=201)
                
            else:
                errors = {}
                errors.update(user_form.errors)
                errors.update(intern_form.errors)
                return JsonResponse({'error': errors}, status=400)
        
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# TASK FUNCTIONS
@csrf_exempt
def edit_task_assignment(request, task_assignment_id):
    task_assignment = get_object_or_404(TaskAssignment, task_assignment_id=task_assignment_id)
    if request.method == 'PUT':
        data = request.PUT
        task_assignment.intern_id = data.get('intern_id')
        task_assignment.task_id = data.get('task_id')
        task_assignment.task_status = data.get('task_status')
        task_assignment.date_started = data.get('date_started')
        task_assignment.file_submission = data.get('file_submission')
        task_assignment.save()
        return JsonResponse({'message': 'Task assignment updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def edit_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'PUT':
        data = request.PUT
        task.task_name = data.get('task_name')
        task.task_description = data.get('task_description')
        task.task_date_created = data.get('task_date_created')
        task.task_due_date = data.get('task_due_date')
        task.task_estimated_time_to_finish = data.get('task_estimated_time_to_finish')
        task.task_points = data.get('task_points')
        task.save()
        return JsonResponse({'message': 'Task updated successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_task_and_assignment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_form = TaskForm(data)
            
            if task_form.is_valid():
                task = task_form.save()  # Save the Task object to get the task_id
                task_id = task.task_id  # Retrieve the task_id from the saved Task object
                interns = data.get('interns')
                
                for intern_id in interns:
                    task_assignment_data = {
                        'intern_id': intern_id,
                        'task_id': task_id,
                        'task_status': data.get('task_status', 'Not Started'),
                        'date_started': data.get('date_started'),
                        'file_submission': data.get('file_submission')
                    }
                    task_assignment_form = TaskAssignmentForm(task_assignment_data)
                    if task_assignment_form.is_valid():
                        task_assignment_form.save()
                    else:
                        return JsonResponse({'error': task_assignment_form.errors}, status=400)
                
                return JsonResponse({'message': 'Task and Task Assignments created successfully'}, status=201)
                
            else:
                return JsonResponse({'error': task_form.errors}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = request.POST
        task = Task(
            task_id=data.get('task_id'),
            task_name=data.get('task_name'),
            task_description=data.get('task_description'),
            task_date_created=data.get('task_date_created'),
            task_due_date=data.get('task_due_date'),
            task_estimated_time_to_finish=data.get('task_estimated_time_to_finish'),
            task_points=data.get('task_points')
        )
        task.save()
        return JsonResponse({'message': 'Task created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_task_assignment(request):
    if request.method == 'POST':
        data = request.POST
        task_assignment = TaskAssignment(
            task_assignment_id=data.get('task_assignment_id'),
            intern_id=data.get('intern_id'),
            task_id=data.get('task_id'),
            task_status=data.get('task_status'),
            date_started=data.get('date_started'),
            file_submission=data.get('file_submission')
        )
        task_assignment.save()
        return JsonResponse({'message': 'Task assignment created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
# Return all task assignments as a list
@csrf_exempt
def get_all_task_assignment(request):
    task_assignments = []
    task_assignments_queryset = TaskAssignment.objects.all()
    for task_assignment in task_assignments_queryset:
        task_assignment_dict = {
            'id': task_assignment.id,
            'intern_id': task_assignment.intern_id.id,
            'task_id': task_assignment.task_id.task_id,
            'task_status': task_assignment.task_status,
            'date_started': task_assignment.date_started,
            'file_submission': task_assignment.file_submission
        }
        task_assignments.append(task_assignment_dict)
    return JsonResponse(task_assignments, safe=False)

# Return all tasks as a list
@csrf_exempt
def get_all_task(request):
    tasks = []
    tasks_queryset = Task.objects.all()
    for task in tasks_queryset:
        task_dict = {
            'task_id': task.task_id,
            'task_name': task.task_name,
            'task_description': task.task_description,
            'task_date_created': task.task_date_created,
            'task_due_date': task.task_due_date,
            'task_estimated_time_to_finish': task.task_estimated_time_to_finish,
            'task_points': task.task_points
        }
        tasks.append(task_dict)
    return JsonResponse(tasks, safe=False)

# Return a specific task assignment by ID
@csrf_exempt
def get_task_assignment(request, task_assignment_id):
    task_assignment = TaskAssignment.objects.get(id=task_assignment_id)
    task_assignment_dict = {
        'id': task_assignment.id,
        'intern_id': task_assignment.intern_id.id,
        'task_id': task_assignment.task_id.task_id,
        'task_status': task_assignment.task_status,
        'date_started': task_assignment.date_started,
        'file_submission': task_assignment.file_submission
    }
    return JsonResponse(task_assignment_dict)

# Return a specific task by ID
@csrf_exempt
def get_task(request, task_id):
    task = Task.objects.get(task_id=task_id)
    task_dict = {
        'task_id': task.task_id,
        'task_name': task.task_name,
        'task_description': task.task_description,
        'task_date_created': task.task_date_created,
        'task_due_date': task.task_due_date,
        'task_estimated_time_to_finish': task.task_estimated_time_to_finish,
        'task_points': task.task_points
    }
    return JsonResponse(task_dict)

@csrf_exempt
def delete_task_assignment(request, id):
    task_assignment = get_object_or_404(TaskAssignment, task_assignment_id=id)
    if request.method == 'DELETE':
        task_assignment.delete()
        return JsonResponse({'message': 'Task assignment deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    if request.method == 'DELETE':
        # Delete the task and all connected task assignments
        task_assignments = TaskAssignment.objects.filter(task_id=id)
        task_assignments.delete()
        task.delete()
        return JsonResponse({'message': 'Task and connected task assignments deleted successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
@csrf_exempt
def handle_vercel_request(request):
    if request.method == 'GET':
        data = {
            'message': 'Hello from Django!',
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
# Workload CRUD views

def workload_list(request):
    workloads = Workload.objects.all()
    return render(request, 'workload_list.html', {'workloads': workloads})

def workload_detail(request, workload_id):
    workload = get_object_or_404(Workload, pk=workload_id)
    return render(request, 'workload_detail.html', {'workload': workload})

def workload_create(request):
    if request.method == 'POST':
        form = WorkloadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workload_list')
    else:
        form = WorkloadForm()
    return render(request, 'workload_form.html', {'form': form})

def workload_update(request, workload_id):
    workload = get_object_or_404(Workload, pk=workload_id)
    if request.method == 'POST':
        form = WorkloadForm(request.POST, instance=workload)
        if form.is_valid():
            form.save()
            return redirect('workload_list')
    else:
        form = WorkloadForm(instance=workload)
    return render(request, 'workload_form.html', {'form': form})

def workload_delete(request, workload_id):
    workload = get_object_or_404(Workload, pk=workload_id)
    if request.method == 'POST':
        workload.delete()
        return redirect('workload_list')
    return render(request, 'workload_confirm_delete.html', {'workload': workload})

# Concern CRUD views

def get_concerns(request):
    concerns = Concern.objects.all()
    concerns_data = [
        {
            'concern_id': concern.concern_id,
            'concern_description': concern.concern_description,
            'academic_workload': concern.academic_workload,
            'other_commitments': concern.other_commitments,
            'date_filed': concern.date_filed.isoformat(),
        } for concern in concerns
    ]
    return JsonResponse(concerns_data, safe=False)

def concern_detail(request, concern_id):
    concern = get_object_or_404(Concern, pk=concern_id)
    concern_data = {
        'concern_id': concern.concern_id,
        'concern_description': concern.concern_description,
        'academic_workload': concern.academic_workload,
        'other_commitments': concern.other_commitments,
        'date_filed': concern.date_filed.isoformat(),
    }
    return JsonResponse(concern_data, safe=False)

@csrf_exempt
def create_concern(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            intern_id = data.get('intern_id')
            intern = get_object_or_404(UserAccount, pk=intern_id)
            concern_form = ConcernForm(data)
            if concern_form.is_valid():
                concern = concern_form.save(commit=False)
                concern.intern_id = intern
                concern.date_filed = datetime.date.today()
                concern.save()
                return JsonResponse({'message': 'Concerns created successfully'}, status=201)
            else:
                print(concern_form.errors)
                return JsonResponse({'error': 'Invalid form data'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
