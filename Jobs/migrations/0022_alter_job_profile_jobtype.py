# Generated by Django 4.0.4 on 2022-07-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0021_alter_job_profile_jobtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_profile',
            name='jobtype',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default=None, max_length=20, null=True),
        ),
    ]