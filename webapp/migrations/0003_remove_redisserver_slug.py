# Generated by Django 3.0.5 on 2020-04-05 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200405_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redisserver',
            name='slug',
        ),
    ]