# Generated by Django 2.2 on 2019-04-30 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_post',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userimage',
            name='time_post',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
