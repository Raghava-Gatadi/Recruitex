# Generated by Django 4.1.7 on 2023-03-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0017_alter_project_project_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubsribeEmails",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]