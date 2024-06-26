# Generated by Django 5.0.6 on 2024-06-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_rename_salar_employeemodel_salary"),
    ]

    operations = [
        migrations.CreateModel(
            name="MovieModel",
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
                ("movie_name", models.CharField(max_length=50)),
                ("image_url", models.CharField(max_length=300)),
                ("director", models.CharField(max_length=100)),
                ("content", models.CharField(max_length=300)),
                ("release_year", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "MovieModel",
            },
        ),
        migrations.RemoveField(
            model_name="blog",
            name="user",
        ),
        migrations.DeleteModel(
            name="Employeemodel",
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
    ]
