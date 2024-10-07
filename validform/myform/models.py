from django.db import models

class StudentModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mobile_number = models.BigIntegerField()  
    roll_number = models.IntegerField() 
    email = models.EmailField()
    dob = models.DateField() 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
