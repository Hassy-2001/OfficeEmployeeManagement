from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')



#     start of view your employee detail work

def view(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, 'view.html', context)

#     end of view your employee detail work







#     start of new employee addition work

def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        contact_no = int(request.POST['contact_no'])

        new_emp = Employee(first_name = first_name, last_name=last_name,department_id=department,role_id=role,
                           salary=salary,bonus=bonus,contact_no=contact_no,hire_date=datetime.now())
        new_emp.save()
        return redirect("view page")
    elif request.method == 'GET':
        return render(request, 'add.html')
    else:
        return HttpResponse("ALERT!! Cannot add any employee")

#     end of new employee addition work






#     start of remove your employee work

def remove(request,emp_id=0):
    if emp_id:
        try:
            remove_employee = Employee.objects.get(id=emp_id)
            remove_employee.delete()
            return redirect("view page")
        except:
            return redirect("remove page")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'remove.html',context)

#     end of remove your employee work







#     start of filter your employee work

def filter(request):

    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        department = request.POST['department']
        filter_employee = Employee.objects.all()
        if name:
            filter_employee = filter_employee.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if role:
            filter_employee = filter_employee.filter(role__name=role)
        if department:
            filter_employee = filter_employee.filter(department__name=department)
        context = {
            "filter_employee": filter_employee
        }
        print(context)
        return render(request,'view.html',context)

    elif request.method == 'GET':
        return render(request, 'filter.html')
    else:
        return HttpResponse("Syntax Error!!!")




#     end of filter your employee work
