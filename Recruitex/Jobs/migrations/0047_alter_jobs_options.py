# Generated by Django 4.1.7 on 2023-04-05 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0046_alter_jobs_title"),
    ]

    operations = [
        migrations.AlterModelOptions(name="jobs", options={"ordering": ["date"]},),
    ]
