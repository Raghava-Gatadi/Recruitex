# Generated by Django 4.1.7 on 2023-03-31 06:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Jobs", "0034_alter_jobs_recruiter"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobs",
            name="job_applied_users",
            field=models.ManyToManyField(
                blank=True,
                related_name="job_applied_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]