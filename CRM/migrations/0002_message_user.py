# Generated by Django 4.0.3 on 2022-04-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
