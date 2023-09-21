# Generated by Django 4.2.5 on 2023-09-20 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("thumbnail", models.ImageField(upload_to="thumbnails/")),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Video",
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
                ("vimeo_id", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=150)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField()),
                ("order", models.IntegerField(default=1)),
                ("file", models.FileField(upload_to="uploads/")),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videos",
                        to="content.course",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
    ]