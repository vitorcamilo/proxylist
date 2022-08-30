# Generated by Django 4.1 on 2022-08-27 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IPlist",
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
                ("ipadress", models.CharField(max_length=20)),
                ("port", models.IntegerField()),
                ("protocol", models.CharField(max_length=5)),
                ("anonymity", models.BooleanField()),
                ("country", models.CharField(max_length=30)),
                ("region", models.CharField(max_length=30, null=True)),
                ("city", models.CharField(max_length=30, null=True)),
                ("uptime", models.DecimalField(decimal_places=2, max_digits=10)),
                ("runtime", models.CharField(max_length=4)),
                ("transfer", models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="EditedField",
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
                ("flag_edited", models.BooleanField()),
                (
                    "iplist_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scrape.iplist",
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
