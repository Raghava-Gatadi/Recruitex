# Generated by Django 4.1.7 on 2023-04-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0032_customuser_dob"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="experience",
            field=models.CharField(blank=True, default="", max_length=50, null=True),
        ),
    ]
