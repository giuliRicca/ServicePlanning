# Generated by Django 4.0.1 on 2022-02-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_services', '0002_rename_start_time_servicetime_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='times',
        ),
        migrations.AddField(
            model_name='service',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ServiceTime',
        ),
    ]