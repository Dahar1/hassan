from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets # type: ignore
from rest_framework.authentication import SessionAuthentication # type: ignore
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly # type: ignore

# Create your views here.
class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes= [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes =[IsAdminUser]
    # permission_classes =[IsAuthenticatedOrReadOnly]
    # permission_classes =[DjangoModelPermissions]
    permission_classes =[DjangoModelPermissionsOrAnonReadOnly ]

