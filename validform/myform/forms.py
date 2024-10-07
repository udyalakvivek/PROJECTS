        
from django import forms
from .models import StudentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['first_name', 'middle_name', 'last_name', 'father_name', 'mobile_number', 'roll_number', 'email', 'dob', 'address', 'gender']
        # fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name:'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name:'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name:'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father Name:'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control','type':"number", 'placeholder': 'Enter Mobile Number:'}),
            'roll_number': forms.NumberInput(attrs={'class': 'form-control','type':'number', 'placeholder': 'Enter Roll Number:'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email:'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.RadioSelect(choices=StudentModel.GENDER_CHOICES),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address:'}),
        }
