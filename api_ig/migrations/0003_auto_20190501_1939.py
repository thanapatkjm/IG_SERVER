# Generated by Django 2.2 on 2019-05-01 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_ig', '0002_auto_20190501_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comm',
        ),
    ]
