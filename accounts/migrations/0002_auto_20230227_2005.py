# Generated by Django 2.2.28 on 2023-02-27 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='joinDate',
        ),
    ]
