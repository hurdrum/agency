# Generated by Django 4.0.3 on 2022-04-18 12:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0003_alter_message_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 18, 12, 20, 27, 504264, tzinfo=utc), null=True),
        ),
    ]