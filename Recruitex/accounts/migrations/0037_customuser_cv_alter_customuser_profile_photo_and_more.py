# Generated by Django 4.1.7 on 2023-04-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0036_customuser_languages"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="cv",
            field=models.FileField(
                blank=True,
                default="",
                null=True,
                upload_to="accounts/<django.db.models.fields.CharField>",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="profile_photo",
            field=models.ImageField(
                blank=True,
                default="default_profile.png",
                null=True,
                upload_to="accounts/<django.db.models.fields.CharField>",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(default="", max_length=100, unique=True),
        ),
    ]