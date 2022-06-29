from xml.dom.minidom import CharacterData
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    description_main = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=700)
    adress = models.CharField(max_length=50)
    area = models.IntegerField()
    price = models.IntegerField()
    rooms = models.IntegerField()
    garages = models.IntegerField()
    photo = models.ImageField(upload_to='static/image/products')
    Product_status_choices = [
        ('Аренда','Аренда'),
        ('Продажа','Продажа'),
    ]
    status = models.CharField(max_length=15, choices=Product_status_choices, default='rent')
    pub_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class Price(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    status_choices = [
        ('Аренда','Аренда'),
        ('Продажа','Продажа'),
    ]
    status = models.CharField(max_length=15, choices=status_choices)

    def __str__(self):
        return self.title