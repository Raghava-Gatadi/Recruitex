# Generated by Django 4.1.7 on 2023-03-30 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0022_subscribedusers"),
    ]

    operations = [
        migrations.RenameModel(old_name="Gender", new_name="Gender_type",),
    ]
