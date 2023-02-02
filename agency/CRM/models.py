from email.policy import default
from django.db import models
import pytz

class Message(models.Model):
    message_theme = models.CharField(max_length=40, verbose_name='theme')
    message_text = models.CharField(max_length=1000, verbose_name='text')
    phone = models.CharField(max_length=30)
    Email = models.EmailField()
    data = models.DateTimeField(auto_now_add=True, null = True)

    user = models.IntegerField(null=True)

    def __str__(self):
        return self.message_theme

