from django.db import models
from django_cryptography.fields import encrypt

class Message(models.Model):
    user = models.CharField(
        max_length=1000,
        verbose_name='Username'
    )
    content = encrypt(models.TextField(verbose_name='Content'))
    date = models.DateField(
        max_length=1000,
        verbose_name='Date'
    )
    def __str__(self):
        return str(self.content)