# Generated by Django 5.1 on 2024-08-23 07:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="email",
        ),
    ]
