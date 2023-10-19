from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True,
            'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    city = models.CharField(max_length=40, verbose_name='город', **NULLABLE)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)
