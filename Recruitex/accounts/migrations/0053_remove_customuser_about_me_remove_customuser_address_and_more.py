# Generated by Django 4.1.7 on 2023-04-03 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0052_alter_customuser_slug"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="about_me",),
        migrations.RemoveField(model_name="customuser", name="address",),
        migrations.RemoveField(model_name="customuser", name="age",),
        migrations.RemoveField(model_name="customuser", name="dob",),
        migrations.RemoveField(model_name="customuser", name="facebook_link",),
        migrations.RemoveField(model_name="customuser", name="gender",),
        migrations.RemoveField(model_name="customuser", name="instagram_link",),
        migrations.RemoveField(model_name="customuser", name="interests",),
        migrations.RemoveField(model_name="customuser", name="languages",),
        migrations.RemoveField(model_name="customuser", name="profile_photo",),
        migrations.RemoveField(model_name="customuser", name="salary",),
        migrations.RemoveField(model_name="customuser", name="twitter_link",),
        migrations.RemoveField(model_name="customuser", name="youtube_link",),
        migrations.CreateModel(
            name="UserPersonalInformation",
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
                ("dob", models.DateField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True,
                        default="default_profile.png",
                        null=True,
                        upload_to="accounts/profile_photos",
                    ),
                ),
                (
                    "salary",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Hyderabad, India",
                        max_length=50,
                        null=True,
                    ),
                ),
                ("about_me", models.TextField(blank=True, default="", null=True)),
                (
                    "languages",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "interests",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "facebook_link",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "twitter_link",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "instagram_link",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "youtube_link",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                (
                    "gender",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.gender_type",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="personal_information",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.userpersonalinformation",
            ),
        ),
    ]