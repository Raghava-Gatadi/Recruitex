# Generated by Django 4.1.7 on 2023-03-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0015_remove_jobs_embedded_location_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobs",
            name="embedded_location_url",
            field=models.TextField(blank=True),
        ),
    ]