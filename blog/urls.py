from django.urls import path,include # type: ignore
from blog import views
from rest_framework.routers import DefaultRouter # type: ignore

# creating router object

router= DefaultRouter()

# register studentviewset with router
router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('',include(router.urls)),
]
