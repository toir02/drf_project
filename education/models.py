from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='course/', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    link = models.TextField(verbose_name='ссылка на видео')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
