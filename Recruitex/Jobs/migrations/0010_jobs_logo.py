# Generated by Django 4.1.7 on 2023-03-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0009_alter_jobs_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobs",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
