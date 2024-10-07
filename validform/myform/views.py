from django.shortcuts import render , redirect
from .forms import studentForm
from .models import StudentModel
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect





def home_view(request):
    form = studentForm
    message = ''
    if request.method == 'POST':
        print("POST request received")
        form = studentForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            form = studentForm()
            message ='Student Data saved Successfully'
            return redirect('index_view')
        else:
            print("Form is invalid")
            message ='Student Form is invalid'
    else:
        form = studentForm()
        
    return render(request, 'Home.html', {'form': form,'message':message})

 
 
def data_view(request):
     data = StudentModel.objects.all()
     if request.method =='POST':
         form = studentForm(request.POST)
         if form.is_valid():
             form.save()
             form = studentForm()
        
         else:
             form =studentForm()
     return render(request, 'data.html',{'data':data, })
