# Generated by Django 4.0.5 on 2023-02-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_profile_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='static/image/default-profile.png', null=True, upload_to='profiles/'),
        ),
    ]
