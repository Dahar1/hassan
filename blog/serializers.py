from rest_framework import serializers # type: ignore
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
 class Meta:
    model = Student
    fields = ['id','name','roll','city']  