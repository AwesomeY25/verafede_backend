from django.db import models

class AccountType(models.TextChoices):
    INTERN = 'I', 'Intern'
    DEPT_SUPERVISOR = 'DS', 'Department Supervisor'

class UserAccount(models.Model):
    username = models.CharField(max_length=255)  # Automate first 2 letters of first name + last name + bday in 6 digits
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)  # Set to null if no value
    mid_initial = models.CharField(max_length=255)
    account_type = models.CharField(
        max_length=2,
        choices=AccountType.choices,
        default=AccountType.INTERN
    )  # Set Intern if no response
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Automate
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Intern(models.Model):
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
        ('Prefer Not To Say', 'Prefer Not To Say'),
    ]

    YEAR_LEVEL_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    INTERNSHIP_TYPE_CHOICES = [
        ('Voluntary', 'Voluntary'),
        ('Required', 'Required'),
    ]
    # Auto Add
    intern_id = models.AutoField(primary_key=True, verbose_name='Intern ID')
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='intern')
    department_id = models.IntegerField()
    # Got
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    intern_status = models.CharField(max_length=255)
    # Got
    birthday = models.DateField()
    # Got
    mobile_number = models.CharField(max_length=11)
    # Got
    school = models.CharField(max_length=255)
    # Got
    year_level = models.IntegerField(choices=YEAR_LEVEL_CHOICES)
    # Got
    degree = models.CharField(max_length=255)
    # Got
    internship_type = models.CharField(max_length=20, choices=INTERNSHIP_TYPE_CHOICES)
    # Got
    school_coordinator = models.CharField(max_length=255)
    # Got
    start_date = models.DateField()
    # Got
    end_date = models.DateField()
    # Got
    nda_file = models.CharField(max_length=255, null=True, blank=True)
    # Got
    min_workload_threshold = models.IntegerField(default=5)
    # Got
    max_workload_threshold = models.IntegerField(default=100)
    intern_head_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Intern ID: {self.intern_id}"
    
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField(null=True, blank=True)
    task_date_created = models.DateField()
    task_due_date = models.DateField()
    task_estimated_time_to_finish = models.FloatField()
    task_points = models.IntegerField(default=0)

    def __str__(self):
        return f"Task ID: {self.task_id}"


class TaskAssignment(models.Model):
    intern_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='Intern User ID')
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Task ID')
    task_status_choices = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    ]
    task_status = models.CharField(max_length=20, choices=task_status_choices, verbose_name='Task Status')
    date_started = models.DateField(verbose_name='Date Started', null=True, blank=True)
    file_submission = models.CharField(max_length=255, verbose_name='File Submission', null=True, blank=True)

    def __str__(self):
        return f"Task Assignment ID: {self.id}"


class Department(models.Model):
    department_id = models.AutoField(primary_key=True, verbose_name='Department ID')
    department_name = models.CharField(max_length=255, verbose_name='Department Name')

    def __str__(self):
        return f"Department ID: {self.department_id}, Department Name: {self.department_name}"


class DepartmentSupervisor(models.Model):
    dept_acct = models.ForeignKey(UserAccount, null=True, on_delete=models.CASCADE, verbose_name='Department Supervisor ID')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Department Supervisor - User ID: {self.dept_sup}, Department ID: {self.department}"


class Workload(models.Model):
    class WorkloadTag(models.TextChoices):
        UNDERLOAD = 'Underload', 'Underload'
        MINIMUM_CAPACITY = 'Minimum Capacity', 'Minimum Capacity'
        IN_CAPACITY = 'In Capacity', 'In Capacity'
        MAXIMUM_CAPACITY = 'Maximum Capacity', 'Maximum Capacity'
        OVERLOAD = 'Overload', 'Overload'

    workload_id = models.BigAutoField(primary_key=True)
    intern_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='Intern User ID')
    week_date = models.DateField()
    workload_points = models.PositiveSmallIntegerField(default=0)
    workload_tag = models.CharField(max_length=20, choices=WorkloadTag.choices)

    def __str__(self):
        return f"Workload ID: {self.workload_id}"
    
class Concern(models.Model):
    class AcademicWorkload(models.TextChoices):
        FULL_SEMESTER = 'Full Semester', 'Yes (taking full semester)'
        FEW_CLASSES = 'Few Classes Only', 'Yes (taking few classes only)'
        NO = 'No', 'No'

    concern_id = models.BigAutoField(primary_key=True)
    intern_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name='Intern User ID')
    concern_description = models.TextField()
    academic_workload = models.CharField(max_length=50, choices=AcademicWorkload.choices)
    other_commitments = models.TextField()
    date_filed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Concern ID: {self.concern_id}"