# Generated by Django 4.1.3 on 2022-12-19 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tlaut_apps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Metode",
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
                ("bank", models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="donasi",
            name="metode_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="tlaut_apps.metode",
            ),
        ),
    ]
