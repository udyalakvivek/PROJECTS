from django.db import models

# Create your models here.

class studentModel(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    roll = models.IntegerField()
    address = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    
    
