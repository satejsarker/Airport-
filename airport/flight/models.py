from django.db import models

# Create your models here.

class flight(models.Model):
    airline=models.CharField(max_length=200)
    flight_no=models.CharField(max_length=200,unique=True)
    destination=models.CharField(max_length=200)
    sta=models.TimeField(max_length=200)
    eta=models.TimeField(max_length=200)
    status=models.CharField(max_length=100)

    class Meta:
        db_table='flight'

    def __str__(self):
        return self.airline
    
