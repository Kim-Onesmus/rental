from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=30)
    location = models.TextField(max_length=40)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=200)
    propertyimage = models.FileField(upload_to='covers/',)
    available = models.PositiveIntegerField()
    contact_owner = models.PositiveIntegerField(null=True)
    contact_landlord = models.PositiveIntegerField(null = True)
    
    def __str__(self):
        return self.name