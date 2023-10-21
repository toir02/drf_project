from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def block_inactive_user():
    User.objects.filter(last_login__lt=timezone.now() - timezone.timedelta(days=30)).update(is_active=False)