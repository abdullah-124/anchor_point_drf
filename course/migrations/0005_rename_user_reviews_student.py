# Generated by Django 5.0.1 on 2024-04-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='user',
            new_name='student',
        ),
    ]
