from django.db import models


# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Product(models.Model):
    product= models.TextField(max_length=20, null=False)
    description=  models.CharField(max_length=100)
    price=models.PositiveIntegerField(null=False)
    image= models.ImageField(upload_to=upload_to, blank=True)
        

