from django.db import models

# Create your models here.


class Products(models.Model):
    price=models.IntegerField()
    name=models.CharField(max_length=250)
    description=models.TextField()
    quantity=models.IntegerField(default=0)
    category=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
