# Generated by Django 4.2.7 on 2023-12-07 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_student_add_requirement'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_requirement',
            new_name='Students',
        ),
    ]