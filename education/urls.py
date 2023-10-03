from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import CourseViewSet

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

] + router.urls
