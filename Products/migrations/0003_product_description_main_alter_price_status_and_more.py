# Generated by Django 4.0.3 on 2022-04-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_main',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='status',
            field=models.CharField(choices=[('Аренда', 'Аренда'), ('Продажа', 'Продажа')], max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Аренда', 'Аренда'), ('Продажа', 'Продажа')], default='rent', max_length=15),
        ),
    ]
