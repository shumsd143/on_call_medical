# Generated by Django 3.1.6 on 2021-02-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="created",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
