# Generated by Django 5.0.1 on 2024-02-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="bonus",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="employee",
            name="salary",
            field=models.CharField(max_length=12),
        ),
    ]