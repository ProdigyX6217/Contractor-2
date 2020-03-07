from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    email = models.EmailField(max_length=100)
    upload = models.ImageField(upload_to='business_photos/', height_field=300, width_field= 300)
    rating = models.DecimalField(max_digits=5, decimal_places=2)

    delivery = models.BooleanField(blank=True, null=True)
    reservations = models.BooleanField(blank=True, null=True)
    take_out = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
