from django.db import models

# Create your models here.
class User():
    title = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=100, blank=True)