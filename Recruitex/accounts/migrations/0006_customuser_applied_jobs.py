# Generated by Django 4.1.7 on 2023-03-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0026_alter_jobs_embedded_location_url"),
        ("accounts", "0005_remove_customuser_identifier_alter_customuser_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="applied_jobs",
            field=models.ManyToManyField(to="Jobs.jobs"),
        ),
    ]