# Generated by Django 3.1.7 on 2021-08-08 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20210807_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='schedules',
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='schedule.day'),
            preserve_default=False,
        ),
    ]
