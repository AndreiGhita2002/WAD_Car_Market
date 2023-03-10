# Generated by Django 4.1.7 on 2023-02-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20230227_2005"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profilePicture",
            field=models.ImageField(
                blank=True,
                default="profile1.png",
                null=True,
                upload_to="profile_images",
            ),
        ),
    ]
