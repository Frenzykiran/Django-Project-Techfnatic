# Generated by Django 4.2.1 on 2023-05-18 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("page", "0002_siteconfiguration"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SiteConfiguration",
            new_name="Background_img",
        ),
    ]