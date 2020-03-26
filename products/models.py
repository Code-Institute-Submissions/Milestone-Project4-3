from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    bid_price = models.DecimalField(max_digits=10, decimal_places=3)
    author = models.CharField(max_length=254, default="")
    date_made = models.CharField(max_length=254, default="")
    country_made_in = models.CharField(max_length=254, default="")
    height = models.DecimalField(max_digits=5, decimal_places=1)
    width = models.DecimalField(max_digits=5, decimal_places=1)
    past_owners = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.name