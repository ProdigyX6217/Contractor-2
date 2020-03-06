from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    email = models.EmailField(max_length=100)
    upload = models.ImageField(upload_to='business_photos/', height_field=300, width_field= 300)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Restaurant(Business):
    delivery = models.BooleanField
    reservations = models.BooleanField
    take_out = models.BooleanField
    # business = models.ForeignKey(Business, on_delete=models.CASCADE)
    pass

class Bar(Business):
    reservations = models.BooleanField
    pass

class Club(Business):
    pass

class Gym(Business):
    pass

class Hotel(Business):
    pass

