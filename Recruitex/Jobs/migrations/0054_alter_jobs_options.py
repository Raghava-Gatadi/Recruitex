# Generated by Django 4.1.7 on 2023-04-08 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0053_alter_jobs_options"),
    ]

    operations = [
        migrations.AlterModelOptions(name="jobs", options={"ordering": ["-id"]},),
    ]
