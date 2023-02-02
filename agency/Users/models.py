from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    favourites = models.CharField(max_length=300, blank=True, default='')
    create_data = models.DateField(auto_now_add=True)
    photo = models.ImageField(null = True, blank=True, upload_to='profiles/', default='static/image/default-profile.png')

    def __str__(self):
        return str(self.email)