from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
class UserSignUPForm(UserCreationForm):
    usable_password = None
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Confirm Password")
    class Meta:
        model = User
        fields = ['username', "first_name", "password1", "password2"]  
        widgets = {
            "username" : forms.TextInput(attrs={'placeholder' : "Enter Username", 'class':'form-control'}),
            "first_name" : forms.TextInput(attrs={'placeholder' : "Enter Username", 'class':'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    pass

class UserPasswordChange1(PasswordChangeForm):
    pass

class UserPasswordChange2(SetPasswordForm):
    pass