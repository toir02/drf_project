from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig

app_name = EducationConfig.name

router = DefaultRouter()

urlpatterns = [

] + router.urls
