from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    like = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass

from django.contrib import admin
admin.site.register(Product)