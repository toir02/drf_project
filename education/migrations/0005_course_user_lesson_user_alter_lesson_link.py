# Generated by Django 4.2.5 on 2023-10-09 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0004_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.URLField(verbose_name='ссылка на видео'),
        ),
    ]