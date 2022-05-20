from django.db import models
from django.db.models import IntegerField


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Order(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
