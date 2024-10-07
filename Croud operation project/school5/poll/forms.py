from django import forms
from .models import StudentModel
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class' : "hello"}))
#     address = forms.CharField()
#     roll = forms.IntegerField()
#     school_Name = forms.CharField()
#     login =  forms.CharField()

class StudentForm(forms.ModelForm):
    # login = forms.CharField() 
    class Meta:
        model  = StudentModel
        # fields = ['id', 'name' , 'address', 'roll']
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs= {"placeholder"  :"Enter Name ", "class" : "form-control", 'id' : 'userid'}),
            'address' : forms.TextInput(attrs= {"placeholder"  :"Enter Address ", 'class' : "form-control"}),
            'roll' : forms.TextInput(attrs= {"placeholder"  :"Enter Roll number", "class" : 'form-control'}),
            'school_Name' : forms.TextInput(attrs= {"placeholder"  :"Enter School Name ", "class" :"form-control"}),
        }
        error_messages = {
            "name" : {"required" : "Name is required please enter "},
            "address" : {"required" : "Address is required please enter "},
        }
        help_texts = {
            "name" : "Enter Name Here",
            "address" : "Enter Address Here",
        }



