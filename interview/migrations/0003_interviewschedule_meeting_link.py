# Generated by Django 3.2.9 on 2021-11-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_interviewschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewschedule',
            name='meeting_link',
            field=models.TextField(blank=True),
        ),
    ]