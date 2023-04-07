from django.shortcuts import render
from .models import Student 
from .forms import StudentForm


def stu_view(request):
    form = StudentForm()
    template_name = 'app1/student_form.html'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, template_name, context)

def stu_list(request):
    data = Student.objects.all()
    template_name = 'app1/student_list.html' 
    context = {'data':data}
    return render(request, template_name, context)


