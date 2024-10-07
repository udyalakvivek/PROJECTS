from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserSignUPForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

#user creation form
def sign_up(request):
    if request.method=="POST":
        fm = UserSignUPForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, "Account Created Successfully!")
            return HttpResponseRedirect("/signup")
    else:
        fm = UserSignUPForm()
    return render(request, "signup.html", {'fm' : fm})


# Login Form View
def login_view(request):
    if request.method=="POST":
        fm = AuthenticationForm(request= request,data= request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            user = authenticate(username = uname, password = pwd)
            if user is not None:
                login(request, user=user)
                messages.add_message(request, messages.SUCCESS, "You're logIn Successfully!")
                return HttpResponseRedirect("/profile")
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'fm'  :fm})

#Password Update View
def passwordchangeview1(request):
    if request.method=="POST":
        fm = PasswordChangeForm(user=request.user, data = request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, "Password Updated Successfully!")
            return HttpResponseRedirect("/login")
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, "password1.html", {'fm' : fm})

#Password Update View
def passwordchangeview2(request):
    if request.method=="POST":
        fm = SetPasswordForm(user=request.user, data = request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, "Password Change Successfully!")
            return HttpResponseRedirect("/login")
    else:
        fm = SetPasswordForm(user=request.user)
    return render(request, "password2.html", {'fm' : fm})


def user_profile(request):
    return render(request, 'profile.html')

