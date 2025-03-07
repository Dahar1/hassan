from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets # type: ignore
from rest_framework.authentication import SessionAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore

# Create your views here.
class StudentsModelViewSet1(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes= [SessionAuthentication]
    # permission_classes = []

