from django.contrib import admin
from .models import BaseModel, Department, Position, Skill, Employee, Project

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(Employee)
admin.site.register(Project)

