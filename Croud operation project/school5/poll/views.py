from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .models import StudentModel

# def home(request):
#     if request.method=="POST":
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             nm = form.cleaned_data['name']
#             add = form.cleaned_data['address']
#             roll = form.cleaned_data['roll']
#             sn = form.cleaned_data['school_Name']
#             print(nm, add, roll, sn)
#             stu_data = StudentModel(name = nm, address = add, roll = roll, school_Name =sn)
#             stu_data.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = StudentForm()
#     return render(request, "home.html", {"form" : form})



def home(request):
    dt = StudentModel.objects.all()
    if request.method=="POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm = StudentForm()
    return render(request, "home.html", {"form" : fm, "data" : dt})


#single records view
def get_student(request, id):
    try:
        dt = StudentModel.objects.get(pk = id)
    except StudentModel.DoesNotExist as err:
        a = """<a href="/">Home</a>"""
        return HttpResponse(f"{err} <br> <br> Back to {a}")
    return render(request, 'student.html', {'stu' : dt})



#deleting records of student
def delete_stu(request, id):
    dt = StudentModel.objects.get(pk = id)
    dt.delete()
    return HttpResponseRedirect('/')


#editing Records of stuents
def update_student_view(request, id):
    dt = StudentModel.objects.get(pk = id)
    if request.method == "POST":
        student_form = StudentForm(request.POST , instance=dt)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/')
    else:
        student_form = StudentForm(instance=dt)
    return render(request, 'editstudent.html', {'fm' :student_form })
