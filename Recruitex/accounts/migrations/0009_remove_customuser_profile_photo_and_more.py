# Generated by Django 4.1.7 on 2023-03-26 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0026_alter_jobs_embedded_location_url"),
        (
            "accounts",
            "0008_alter_customuser_applied_jobs_alter_customuser_phone_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="profile_photo",),
        migrations.AlterField(
            model_name="customuser",
            name="applied_jobs",
            field=models.ManyToManyField(to="Jobs.jobs"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="phone",
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
