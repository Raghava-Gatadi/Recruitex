# Generated by Django 4.1.7 on 2023-03-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0025_job_duration_type_jobs_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="embedded_location_url",
            field=models.TextField(
                blank=True, help_text="Embeded url from maps of company only src"
            ),
        ),
    ]