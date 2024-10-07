from django import forms
from .models import studentModel


class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'
        
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Student Name:'}),
            'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Father Name:'}),
            'roll':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Roll No.:'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Student Add::'}),
            'school_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter School Name:'}),
        }
    