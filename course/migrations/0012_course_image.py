# Generated by Django 5.0.1 on 2024-04-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_enroll'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='course/images/'),
        ),
    ]
