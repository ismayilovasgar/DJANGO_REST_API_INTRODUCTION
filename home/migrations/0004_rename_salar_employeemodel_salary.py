# Generated by Django 5.0.6 on 2024-06-12 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_employeemodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employeemodel",
            old_name="salar",
            new_name="salary",
        ),
    ]