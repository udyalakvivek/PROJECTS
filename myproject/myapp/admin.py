from django.contrib import admin
from .models import studentModel

# Register your models here.

@admin.register(studentModel)
class studentModelAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'fname', 'roll', 'address', 'school_name']
    

