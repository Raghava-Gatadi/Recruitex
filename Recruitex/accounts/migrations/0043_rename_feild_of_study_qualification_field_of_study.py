# Generated by Django 4.1.7 on 2023-04-03 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0042_remove_qualification_location_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="qualification",
            old_name="feild_of_study",
            new_name="field_of_study",
        ),
    ]
