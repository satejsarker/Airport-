from django.db import models

# Create your models here.
class bus(models.Model):
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    dep=models.TimeField(max_length=200)
    ar=models.TimeField(max_length=200)
    
    class Meta:
        db_table='bus'
    def __str__(self):
        return self.origin