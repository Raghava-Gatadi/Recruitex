# Generated by Django 4.1.7 on 2023-03-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0011_remove_jobs_logo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("about_you", models.TextField(blank=True, null=True)),
                ("why_you", models.TextField()),
            ],
        ),
    ]
