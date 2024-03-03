# Generated by Django 5.0.1 on 2024-02-11 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_department_alter_intern_intern_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentSupervisor',
            fields=[
                ('sup_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='User ID')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.department', verbose_name='Department ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.useraccount', verbose_name='User ID')),
            ],
        ),
    ]