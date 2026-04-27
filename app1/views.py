from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from  app1.models import Student
from app1.forms import student_form

from django.http import HttpResponse
from app1.forms import student_delete

from app1.forms import student_delete

# create
def student_list(request):
    data=Student.objects.all()
    form=student_form()

    if request.method=="POST":
        form=student_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request,'student_list.html',{'data':data,'form':form})


# update

def student_update(request,id):
    student=get_object_or_404(Student,id=id)
    form=student_form(instance=student)

    if request.method=="POST":
        form=student_form(request.POST,instance=student)

        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    return render(request,'student_update.html',{'form':form})


# delete

def delete_std(request, id):
    std = Student.objects.get(id=id)

    if request.method == "POST":
        form = student_delete(request.POST)

        if form.is_valid():
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if user == "vivek" and password == "vivek123":
                std.delete()
                return redirect('home_page')
            else:
                return HttpResponse("<h1>Invalid username/password</h1>")
    else:
        form = student_delete()

    return render(request, 'delete_std.html', {'del_form': form})