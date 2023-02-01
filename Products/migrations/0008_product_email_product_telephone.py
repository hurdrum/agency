# Generated by Django 4.0.5 on 2023-02-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_job_delete_price_remove_product_garages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='product',
            name='telephone',
            field=models.CharField(max_length=50, null=True, verbose_name='Телефон'),
        ),
    ]