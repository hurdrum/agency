# Generated by Django 4.0.3 on 2022-04-12 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='data',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 4, 12, 11, 57, 41, 477182, tzinfo=utc)),
        ),
    ]
