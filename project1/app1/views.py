from django.shortcuts import render
from .models import Student 
from .forms import StudentForm


def stu_view(request):
    template_name = ''
    context = {}
    return render(request, template_name, context)


