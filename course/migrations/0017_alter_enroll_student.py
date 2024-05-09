# Generated by Django 5.0.1 on 2024-05-09 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_remove_enroll_course_enroll_course'),
        ('student', '0003_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
