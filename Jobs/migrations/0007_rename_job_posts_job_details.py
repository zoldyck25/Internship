# Generated by Django 4.0.4 on 2022-07-07 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0006_alter_job_posts_jobtype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='job_posts',
            new_name='job_details',
        ),
    ]