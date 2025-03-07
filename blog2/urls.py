from django.urls import path,include # type: ignore
from .views import *
from rest_framework.routers import DefaultRouter # type: ignore

# creating router object

router= DefaultRouter()

# register studentviewset with router
router.register('studentsapi',StudentsModelViewSet1,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),

]
