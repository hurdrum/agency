from email.policy import default
from django.db import models
from django.utils import timezone
import pytz

class Message(models.Model):
    timezone.activate(pytz.timezone('Europe/Moscow'))
    message_theme = models.CharField(max_length=40, verbose_name='theme')
    message_text = models.CharField(max_length=1000, verbose_name='text')
    phone = models.CharField(max_length=30)
    Email = models.EmailField()
    data = models.DateTimeField(default=timezone.now(), null = True)

    user = models.IntegerField(null=True)

    def __str__(self):
        return self.message_theme

