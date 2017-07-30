from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class shop(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField();
    location=models.CharField(max_length=150)
    contact=PhoneNumberField()
    class Meta:
        db_table='shop'
    def __str__(self):
        return self.title
