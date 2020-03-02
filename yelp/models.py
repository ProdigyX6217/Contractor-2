from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField
    price = models.IntegerField
    id = models.BigIntegerField
    # product_photos = models.ImageField((upload_to=None, height_field=None, width_field=None, max_length=100)
    delivery = models.BooleanField
    reservations = models.BooleanField
    