# Generated by Django 4.0.4 on 2022-07-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0013_rename_job_details_job_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='job_profile',
            name='jobtype',
            field=models.CharField(choices=[('full-time', 'full-time'), ('part-time', 'part-time')], default=None, max_length=20, null=True),
        ),
    ]
