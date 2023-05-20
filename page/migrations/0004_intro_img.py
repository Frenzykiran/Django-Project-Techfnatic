# Generated by Django 4.2.1 on 2023-05-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0003_rename_siteconfiguration_background_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="intro_img",
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
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
            ],
        ),
    ]
