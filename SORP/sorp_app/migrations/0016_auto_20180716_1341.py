# Generated by Django 2.0.6 on 2018-07-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0015_auto_20180715_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='religion',
            field=models.CharField(choices=[('---------', '---------'), ('Christian', 'Christian'), ('Hinduism', 'Hinduism'), ('Jainism', 'Jainism'), ('Muslim', 'Muslim'), ('Buddhism', 'Buddhism'), ('Sikhism', 'Sikhism'), ('Judaism', 'Judaism'), ('Zoroastrianism', 'Zoroastrianism')], max_length=16),
        ),
    ]