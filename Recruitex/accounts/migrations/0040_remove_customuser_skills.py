# Generated by Django 4.1.7 on 2023-04-02 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0039_customuser_resume_alter_customuser_cv"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="skills",),
    ]
