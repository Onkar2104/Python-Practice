# Generated by Django 4.2.15 on 2024-08-26 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_subject_subjectmarks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['department', 'student_name'], 'verbose_name': 'student'},
        ),
    ]
