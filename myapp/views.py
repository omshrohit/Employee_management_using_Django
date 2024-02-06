from django.shortcuts import render
from django.http import HttpResponse
from .models import employee,Department,Role
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'./index.html')

def all_enp(request):
    emps=employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,'./all_employee.html',context=context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        role=request.POST['role']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone'] 
        hire_date=request.POST['hire_date']
        new_emp=employee.objects.create(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,phone=phone,hire_date=hire_date)
        return HttpResponse("<p>successfull add</p>")
    return render(request,'./add_emp.html')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("<h1>Successfully Delete</h1>")
        except:
            return HttpResponse("<h1>please enter valid Emp id")
    emps=employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'./remove_emp.html',context=context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']

        emps=employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))

        if dept:
            emps=emps.filter(dept__name__icontains=dept)

        if role:
            emps=emps.filter(role__name__icontains=role)

        context={
            'emps':emps
        }

        return render(request,'./all_employee.html',context=context)
    return render(request,'./filter_emp.html')