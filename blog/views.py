from django.shortcuts import render # type: ignore
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets # type: ignore
from rest_framework.authentication import BasicAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser # type: ignore
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes= [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes =[IsAdminUser]
   
     

    # this second no class access anybody without register
