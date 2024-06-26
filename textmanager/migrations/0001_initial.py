# Generated by Django 4.1.3 on 2024-05-17 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("unique_id", models.CharField(max_length=255, unique=True)),
                ("title", models.CharField(max_length=255, unique=True)),
                ("groups", models.ManyToManyField(blank=True, to="auth.group")),
            ],
            options={
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Language",
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
                ("alpha2", models.CharField(max_length=2, unique=True)),
                ("alpha3_b", models.CharField(max_length=3, unique=True)),
                ("english_name", models.CharField(max_length=30, unique=True)),
                ("language_name", models.CharField(max_length=30, unique=True)),
                ("flag", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Text",
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
                    "unique_id",
                    models.CharField(
                        blank=True, max_length=255, null=True, unique=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="textmanager.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LanguageText",
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
                ("value", models.TextField()),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="textmanager.language",
                    ),
                ),
                (
                    "text",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="textmanager.text",
                    ),
                ),
            ],
            options={
                "unique_together": {("language", "text")},
            },
        ),
    ]
