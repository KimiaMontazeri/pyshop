from django.db import models


# by inheriting Model class, we are able to store a Product in a database
class Product(models.Model):
    # CharField means a field that can store characters
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
