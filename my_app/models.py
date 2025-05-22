from django.db import models

# Create your models here.


class Property(models.Model):
    Address = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    city = models.CharField(max_length=200)  # California, USA
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    emailaddress = models.CharField(max_length=200)
    clients_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_lenght=500)
