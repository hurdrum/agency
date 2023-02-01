from xml.dom.minidom import CharacterData
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    description_main = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=700)
    adress = models.CharField(max_length=50)
    area = models.IntegerField()
    price = models.IntegerField()
    Product_status_choices = [
        ('Аренда','Аренда'),
        ('Продажа','Продажа'),
    ]
    status = models.CharField(max_length=15, choices=Product_status_choices, default='rent')
    pub_date = models.DateField(auto_now=False, auto_now_add=True)
    isVIP = models.BooleanField()
    telephone = models.CharField(("Телефон"), max_length=50, null=True)
    Email = models.EmailField(("Email"), max_length=254, null=True)
    users = models.ManyToManyField(User, related_name='favorite_prods')

    def __str__(self):
        return self.title
    def get_images(self):
        return self.image_set.all()
    class Meta:
        ordering = ['-pub_date']

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/image/products/')

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    pay = models.IntegerField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.title