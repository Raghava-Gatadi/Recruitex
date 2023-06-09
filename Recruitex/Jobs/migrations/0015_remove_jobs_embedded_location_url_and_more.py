# Generated by Django 4.1.7 on 2023-03-24 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0014_jobs_embedded_location_url_alter_jobs_location"),
    ]

    operations = [
        migrations.RemoveField(model_name="jobs", name="embedded_location_url",),
        migrations.AlterField(
            model_name="jobs",
            name="location",
            field=models.CharField(
                help_text="Enter company's embedded location from Google",
                max_length=255,
            ),
        ),
    ]
