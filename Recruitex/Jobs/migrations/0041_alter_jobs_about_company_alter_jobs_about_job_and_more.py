# Generated by Django 4.1.7 on 2023-04-05 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0040_alter_jobs_designation_alter_jobs_salary_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="about_company",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="about_job",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobs", name="date", field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="designation",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="job_Category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Jobs.tag",
            ),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="job_duration_type",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Jobs.job_duration",
            ),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="location",
            field=models.CharField(
                blank=True,
                help_text="Enter company's location (city name)",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="logo",
            field=models.ImageField(
                blank=True, default="", null=True, upload_to="Jobs/job_logo"
            ),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="no_of_openings",
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="salary",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="title",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="workings",
            field=models.TextField(blank=True, null=True),
        ),
    ]