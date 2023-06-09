# Generated by Django 4.1.7 on 2023-04-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0040_remove_customuser_skills"),
    ]

    operations = [
        migrations.CreateModel(
            name="Qualification",
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
                ("institute_name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("degree_type", models.CharField(max_length=255)),
                ("feild_of_study", models.CharField(max_length=255)),
                ("start_year", models.IntegerField()),
                ("end_year", models.IntegerField()),
                ("score", models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="qualifications",
            field=models.ManyToManyField(
                blank=True, null=True, to="accounts.qualification"
            ),
        ),
    ]
