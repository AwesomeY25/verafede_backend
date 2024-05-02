from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include
from users import views as userviews

urlpatterns = [
    path('',  csrf_exempt(userviews.log_in), name='log_in'),
    path('admin/', admin.site.urls),
        
    # User URLs
    path('user/add/', csrf_exempt(userviews.create_user), name='create_user'),
    path('users/', csrf_exempt(userviews.get_all_user), name='get_all_user'),
    path('user/<int:id>/', csrf_exempt(userviews.get_user), name='get_user'),  # Changed user_detail to get_user
    path('user/delete/<int:id>/', csrf_exempt(userviews.delete_user), name='delete_user'),
    path('user/update/<int:id>/', userviews.update_user, name='update_user'),  # Changed update_user to edit_user
    
    # Intern URLs
    path('intern/add/', csrf_exempt(userviews.create_intern), name='create_intern'),
    path('interns/', csrf_exempt(userviews.get_all_intern), name='get_all_intern'),  # Changed get_all_intern to list_interns
    path('intern/<int:intern_id>/', userviews.get_intern, name='get_intern'),
    path('intern/delete/<int:intern_id>/', userviews.delete_intern, name='delete_intern'),
    path('intern/update/<int:intern_id>/', userviews.update_intern, name='update_intern'),

    # User and Intern URLs
    path('user/', include('users.api.urls')),
    path('new/', csrf_exempt(userviews.create_user_and_intern), name='create_user_and_intern'),
    
    # Task URLs
    path('task/add/', csrf_exempt(userviews.create_task_and_assignment), name='create_task_and_assignment'),
    path('assign/new/<int:id>/', csrf_exempt(userviews.create_task_assignment), name='create_task_assignment'),
    path('assign/delete/<int:id>/', csrf_exempt(userviews.delete_task_assignment), name='delete_task_assignment'),
    path('task/delete/<int:task_id>/', userviews.delete_task, name='delete_task'), 
    path('assign/update/<int:id>/', userviews.edit_task_assignment, name='edit_task_assignment'), 
    path('task/update/<int:id>/', userviews.edit_task, name='edit_task'), 
    path('tasks/', csrf_exempt(userviews.get_all_task), name='get_all_task'),  
    path('tasks/assigned/', csrf_exempt(userviews.get_all_task_assignment), name='get_all_task_assignment'),
    path('task/done/<int:id>/', csrf_exempt(userviews.mark_done), name='mark_done'), 
    path('task/undone/<int:id>/', csrf_exempt(userviews.mark_undone), name='mark_undone'), 
    path('task/<int:id>/', csrf_exempt(userviews.get_task), name='get_task'), 

    path('task/assign/<int:id>/', csrf_exempt(userviews.get_task_assignment), name='get_task_and_assignment'),  # getting all assigned task to a person (id)
    path('handle-vercel-request/', csrf_exempt(userviews.handle_vercel_request), name='handle_vercel_request'),
    
    # Concern URLs
    path('concern/add/', csrf_exempt(userviews.create_concern), name='create_concern'),  # Added create_concern
    path('concerns/', csrf_exempt(userviews.get_concerns), name='get_concerns'),  # Added get_concerns
    path('concern/<int:id>/', csrf_exempt(userviews.concern_detail), name='concern_detail'),  # Added get_concerns
    
    # Workload URLs
    path('workloads/', userviews.workload_list, name='workload_list'),
    path('workload/<int:workload_id>/', userviews.workload_detail, name='workload_detail'),# Added get_workloads
    path('workloads/new/', userviews.create_workload, name='create_workload'),
    path('workloads/intern/<int:id>/', userviews.intern_workload, name='intern_workload'),
    
    path('unverified/', userviews.get_unverified_interns, name='get_unverified_interns'),
    path('intern/status/<int:intern_id>/', userviews.update_intern_status, name='update_intern_status'),
    path('verify/<int:intern_id>/', userviews.verify_intern, name='verify_intern'),
    path('decline/<int:intern_id>/', userviews.decline_intern, name='decline_intern'),
    path('all_interns/<int:department_id>/', userviews.get_department_interns, name='get_department_interns'),
]