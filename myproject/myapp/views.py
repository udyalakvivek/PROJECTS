from django.shortcuts import render
from .forms import studentForm
from .models import studentModel
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

# to data save 

def student_view(request):
    form = studentForm
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            form = studentForm()
        else:
            form = studentForm()
    return render(request, 'student_view.html', {'form': form})



# to data view
def student_data(request):
    data = studentModel.objects.all()
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            form = studentForm()
        else:
            form = studentForm()
    return render(request, 'student_data.html', {'data': data , 'form':form})


#Delete  student Records 

def student_delete(request , id):
    data = studentModel.objects.get(pk = id)
    data.delete()
    
    return  HttpResponseRedirect('/student_data')


#view single data 

def single_view(request, id):
    dt = studentModel.objects.get(pk = id)
    return render(request, 'single_data.html', {'single_data': dt})




#update Student student
# def update_data(request, id):
    
#     dt = studentModel.objects.get(pk=id)
#     if request.method == "POST":
#         student_form = studentForm(request.POST, instance = dt)
#         if student_form.is_valid():
#             student_form.save()
#             return HttpResponseRedirect('/')
#     else:
#         student_form = studentForm(instance = dt)
#         return render(request, 'update.html',{'fm_data':student_form})

def update_data(request, id):
    dt = studentModel.objects.get(pk = id)
   
    if request.method == 'POST':
        stu = studentForm(request.POST, instance=dt)
        if stu.is_valid():
            stu.save()
            return HttpResponseRedirect('/student_data')
    else:
        stu = studentForm(instance=dt)
        return render(request, 'update_data.html', {'fm_data':stu})