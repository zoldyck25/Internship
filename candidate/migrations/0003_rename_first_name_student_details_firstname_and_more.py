# Generated by Django 4.0.4 on 2022-06-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_rename_jobtitle_student_details_jobposition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='student_details',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='student_details',
            old_name='middle_name',
            new_name='middlename',
        ),
    ]
