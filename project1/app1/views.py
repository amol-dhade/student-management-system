from django.shortcuts import render, redirect
from .models import Student 
from .forms import StudentForm


def stu_view(request):
    form = StudentForm()
    template_name = 'app1/student_form.html'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list_url')
    context = {'form':form}
    return render(request, template_name, context)

def stu_list(request):
    data = Student.objects.all()
    template_name = 'app1/student_list.html' 
    context = {'data':data}
    return render(request, template_name, context)

def update_student(request, pk):
    obj = Student.objects.get(pk=pk)
    form = StudentForm(instance=obj)
    template_name = 'app1/student_form.html'
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('student_list_url')
    context = {'form':form}
    return render(request, template_name, context)

def delete_student(request, pk):
    obj = Student.objects.get(pk=pk)
    template_name = 'app1/delete_student.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('student_list_url')
    return render(request, template_name)






