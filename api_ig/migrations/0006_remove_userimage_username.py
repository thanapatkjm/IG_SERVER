# Generated by Django 2.1.1 on 2019-05-06 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_ig', '0005_userimage_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='username',
        ),
    ]