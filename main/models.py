from django.db import models

from django.db import models

class Servise(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    icon = models.ImageField()

class About(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()

class TrackShipment(models.Model):
    title = models.CharField(max_length = 255)
    number = models.SmallIntegerField()
    icon = models.ImageField()

class Client(models.Model):
    name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    text = models.TextField()
    icon = models.ImageField()

class Form(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 14)
    massage = models.TextField()

    
    # def __str__(self):
    #     return f"{self.name}"
    

    # class Meta:
    #     verbose_name = ""
    #     verbose_name_plural = ""
    #     ordering = ("")

