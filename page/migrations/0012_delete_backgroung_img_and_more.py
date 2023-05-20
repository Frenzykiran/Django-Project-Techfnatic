# Generated by Django 4.2.1 on 2023-05-19 08:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0011_backgroung_img_company_name_delete_company_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Backgroung_img",
        ),
        migrations.RemoveField(
            model_name="background_img",
            name="background_image_url",
        ),
        migrations.RemoveField(
            model_name="background_img",
            name="company_name",
        ),
        migrations.AddField(
            model_name="background_img",
            name="Back_img",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/",
                validators=[django.core.validators.FileExtensionValidator(["jpg"])],
            ),
        ),
    ]
