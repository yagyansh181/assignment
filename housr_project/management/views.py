from django.shortcuts import render

# Create your views here.

from .models import *


def homepage(request):
    return render(request, 'management/homepage.html')


def manage_permissions(request):
    employees = Employee.objects.all()
    groups = Group.objects.all()
    permissions = Permission.objects.all()

    if request.method == 'POST':
        for employee in employees:
            employee_groups = request.POST.getlist(f'groups_{employee.id}')
            employee.assigned_groups.set(employee_groups)
            employee.save()

    return render(request, 'management/manage_permissions.html', {
        'employees': employees,
        'groups': groups,
        'permissions': permissions,
    })
