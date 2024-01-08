from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(BaseModel):
    department_image = models.ImageField(upload_to='department_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Position(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Skill(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    hire_date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(BaseModel):
    project_image = models.ImageField(upload_to='proj_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    employees = models.ManyToManyField(Employee)

    def __str__(self):
        return self.name