# Generated by Django 5.0.1 on 2024-04-30 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
