# Generated by Django 4.1.7 on 2023-03-20 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Jobs", "0007_alter_jobs_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]