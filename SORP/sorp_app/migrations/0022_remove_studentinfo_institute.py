# Generated by Django 2.0.6 on 2018-07-15 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0021_auto_20180715_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='institute',
        ),
    ]