# Generated by Django 5.0.1 on 2024-02-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_employee_bonus_alter_employee_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="phone",
            field=models.CharField(max_length=12),
        ),
    ]