from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [

] + router.urls
