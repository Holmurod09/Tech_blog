from django.db import models

class Gadgets(models.Model):
    images = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=100)

