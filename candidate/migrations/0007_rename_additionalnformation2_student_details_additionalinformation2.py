# Generated by Django 4.0.4 on 2022-06-30 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_rename_address_student_details_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_details',
            old_name='additionalnformation2',
            new_name='additionalInformation2',
        ),
    ]
