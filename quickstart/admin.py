from django.contrib import admin
from django.contrib.auth.models import User, Group
from quickstart.models import University, Student
# Register your models here.

admin.site.register(University)
admin.site.register(Student)