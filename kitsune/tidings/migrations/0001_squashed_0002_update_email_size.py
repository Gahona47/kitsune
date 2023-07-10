# Generated by Django 4.1.7 on 2023-04-18 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Watch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("event_type", models.CharField(db_index=True, max_length=30)),
                ("object_id", models.PositiveIntegerField(db_index=True, null=True)),
                ("email", models.EmailField(blank=True, db_index=True, max_length=254, null=True)),
                ("secret", models.CharField(blank=True, max_length=10, null=True)),
                ("is_active", models.BooleanField(db_index=True, default=False)),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WatchFilter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("value", models.PositiveIntegerField()),
                (
                    "watch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="filters",
                        to="tidings.watch",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "watch")},
            },
        ),
    ]