# Generated by Django 4.0.4 on 2022-07-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0023_alter_student_details_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='pnumber',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_details',
            name='skillsproficiency',
            field=models.IntegerField(default=232),
            preserve_default=False,
        ),
    ]
