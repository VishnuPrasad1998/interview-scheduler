# Generated by Django 3.2.9 on 2021-11-10 13:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_start_time', models.TimeField()),
                ('scheduled_end_time', models.TimeField()),
                ('scheduled_date', models.DateField()),
                ('posting_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('interviewee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='interview.interviewee')),
                ('interviewer', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='interview.interviewer')),
            ],
        ),
    ]
