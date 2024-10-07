from django.contrib import admin
from .models import StudentModel

# Register your models here.
@admin.register(StudentModel)
class StudentModelAdmin(admin.ModelAdmin):
    list_display =[
        'id', 
        'first_name', 
        'middle_name',
        'last_name',
        'father_name', 
        'mobile_number',
        'roll_number',
        'email',
        'dob', 
        'gender', 
        'address', 
        ]
    
