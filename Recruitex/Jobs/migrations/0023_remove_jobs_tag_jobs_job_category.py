# Generated by Django 4.1.7 on 2023-03-24 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0022_remove_jobs_category_jobs_tag_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="jobs", name="tag",),
        migrations.AddField(
            model_name="jobs",
            name="job_Category",
            field=models.ForeignKey(
                default=None, on_delete=django.db.models.deletion.CASCADE, to="Jobs.tag"
            ),
        ),
    ]
