# Generated by Django 3.2.7 on 2021-09-16 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_submission_student'),
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClassroomUser',
        ),
    ]
