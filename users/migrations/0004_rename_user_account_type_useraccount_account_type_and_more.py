# Generated by Django 5.0.1 on 2024-02-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_intern_id_remove_useraccount_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_account_type',
            new_name='account_type',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_middle_initial',
            new_name='mid_initial',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_timestamp',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_username',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
