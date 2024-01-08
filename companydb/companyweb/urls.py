from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('employee.html', views.employee_view, name='employee'),
    path('department.html', views.department_view, name='department'),
    path('position.html', views.position_view, name='position'),
    path('project.html', views.project_view, name='project'),
    path('skill.html', views.skill_view, name='skill'),
]