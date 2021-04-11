from django.db import models
from django_cryptography.fields import encrypt

class Message(models.Model):
    user_from = models.CharField(
        max_length=1000,
        verbose_name='From user'
    )
    user_to = models.CharField(
        max_length=1000,
        verbose_name='To user'
    )
    content = encrypt(models.TextField(verbose_name='Content'))
    date = models.DateTimeField(
        max_length=1000,
        verbose_name='Date'
    )
    def __str__(self):
        return str(self.content)