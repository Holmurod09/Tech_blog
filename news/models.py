from django.db import models

class Gadgets(models.Model):
    images = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Videos(models.Model):
    images = models.ImageField(upload_to="media/")
    faceboook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google = models.URLField(blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.CharField(max_length=100)
    who = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    images = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Contatct(models.Model):
    full_name = models.CharField(max_length=200)
    phohe = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.title



# kwork
# upwork
# React Js (Json --> DRF), Vue js =>) -> Android APP