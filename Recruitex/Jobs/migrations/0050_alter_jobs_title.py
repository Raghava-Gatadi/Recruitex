# Generated by Django 4.1.7 on 2023-04-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0049_alter_jobs_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="title",
            field=models.CharField(blank=True, default="", max_length=250, null=True),
        ),
    ]