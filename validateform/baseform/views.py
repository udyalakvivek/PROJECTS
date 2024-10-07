from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import studentForm

# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            form = studentForm()
            
    else:
        form = studentForm()
        return render(request, 'Form.html', {'form': form})
    
        
