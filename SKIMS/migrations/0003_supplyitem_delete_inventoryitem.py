# Generated by Django 5.1.4 on 2024-12-22 06:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("SKIMS", "0002_alter_category_options_remove_inventoryitem_name_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SupplyItem",
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
                ("supplyName", models.CharField(max_length=255, null=True)),
                ("quantity", models.IntegerField()),
                ("vendor", models.CharField(max_length=255, null=True)),
                ("model", models.CharField(max_length=255, null=True)),
                ("refNum", models.CharField(max_length=255, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "binName",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="SKIMS.binitem",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="SKIMS.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "supplies",
            },
        ),
        migrations.DeleteModel(
            name="InventoryItem",
        ),
    ]