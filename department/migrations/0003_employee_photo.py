# Generated by Django 3.1.7 on 2021-09-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0002_department_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="photo",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
