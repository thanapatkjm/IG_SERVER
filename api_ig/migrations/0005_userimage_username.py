# Generated by Django 2.1.1 on 2019-05-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ig', '0004_auto_20190503_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='username',
            field=models.TextField(default='number1'),
        ),
    ]