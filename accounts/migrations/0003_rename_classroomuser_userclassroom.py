# Generated by Django 3.2.7 on 2021-09-16 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0002_delete_classroomuser'),
        ('accounts', '0002_classroomuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassroomUser',
            new_name='UserClassroom',
        ),
    ]
