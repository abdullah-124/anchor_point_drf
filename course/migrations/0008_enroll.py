# Generated by Django 5.0.1 on 2024-04-30 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_mobile_num'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=12)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('student', models.ManyToManyField(to='student.student')),
            ],
        ),
    ]