# Generated by Django 4.2.1 on 2023-05-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0013_company_delete_company_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="FacebookLink",
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
                ("F_Link", models.TextField()),
                ("flink", models.CharField(max_length=100)),
            ],
        ),
    ]
