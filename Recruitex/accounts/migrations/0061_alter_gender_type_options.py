# Generated by Django 4.1.7 on 2023-04-05 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0060_alter_skills_options_alter_qualification_id_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gender_type", options={"ordering": ["name"]},
        ),
    ]
