from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Employee, Department, Project, Position, Skill
# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def employee_view(request):
    all_employee = Employee.objects.all()
    p = Paginator(all_employee, 5)
    page = request.GET.get('page')
    employee_list = p.get_page(page)
    return render(request, 'employee.html', {'employee': employee_list})

def department_view(request):
    all_department = Department.objects.all()
    p = Paginator(all_department, 4)
    page = request.GET.get('page')
    department_list = p.get_page(page)
    return render(request, 'department.html', {'department': department_list})

def project_view(request):
    all_project = Project.objects.all()
    p = Paginator(all_project, 4)
    page = request.GET.get('page')
    project_list = p.get_page(page)
    return render(request, 'project.html', {'project': project_list})

def position_view(request):
    all_position = Position.objects.all()
    p = Paginator(all_position, 5)
    page = request.GET.get('page')
    position_list = p.get_page(page)
    return render(request, 'position.html', {'position': position_list})

def skill_view(request):
    all_skill = Skill.objects.all()
    p = Paginator(all_skill, 5)
    page = request.GET.get('page')
    skill_list = p.get_page(page)
    return render(request, 'skill.html', {'skill': skill_list})
