from django.db import models

# Create your models here.


class ContactForm(models.Model):
    nickname = models.CharField(max_length=100)
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
