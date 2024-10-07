from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    roll = models.IntegerField()
    school_Name = models.CharField(max_length=20)
    