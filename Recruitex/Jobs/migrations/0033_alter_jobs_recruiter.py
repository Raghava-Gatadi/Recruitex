# Generated by Django 4.1.7 on 2023-03-31 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Jobs", "0032_rename_job_duration_type_job_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="recruiter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recruiter_name",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
