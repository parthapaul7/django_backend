from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    def __str__(self):
        return self.name