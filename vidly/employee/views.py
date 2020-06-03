

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Employee

# Create your views here.
def index(request):
    employee=Employee.objects.all()
    return render(request,'employee/index.html',{'employee':employee})
def detail(request,employee_id):

    employee=get_object_or_404(Employee,pk=employee_id)
    return render(request,'employee/detail.html',{'employee':employee})

