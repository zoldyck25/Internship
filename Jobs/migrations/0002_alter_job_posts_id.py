# Generated by Django 4.0.4 on 2022-07-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_posts',
            name='id',
            field=models.AutoField(default=True, primary_key=True, serialize=False, unique=True),
        ),
    ]
