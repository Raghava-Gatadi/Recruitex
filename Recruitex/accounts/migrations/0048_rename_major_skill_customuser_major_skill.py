# Generated by Django 4.1.7 on 2023-04-03 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0047_alter_customuser_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser", old_name="Major_skill", new_name="major_skill",
        ),
    ]
