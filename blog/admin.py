from django.contrib import admin # type: ignore
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','roll','city','name']
