# Generated by Django 4.2.1 on 2023-05-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0012_delete_backgroung_img_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="company_name",
        ),
    ]
