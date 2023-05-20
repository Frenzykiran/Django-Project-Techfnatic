# Generated by Django 4.2.1 on 2023-05-19 08:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0010_aboutus"),
    ]

    operations = [
        migrations.CreateModel(
            name="Backgroung_img",
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
                    "Back_img",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(["jpg"])
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="company_name",
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
                ("c_name", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Company",
        ),
        migrations.AlterField(
            model_name="aboutus",
            name="about_us",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/",
                validators=[django.core.validators.FileExtensionValidator(["jpg"])],
            ),
        ),
    ]