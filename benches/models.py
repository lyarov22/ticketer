from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from userSystem.models import CustomUser


class BenchType(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Тип')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    avatar = models.ImageField(default='default.png', upload_to='bench_type/', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'

    def __str__(self):
        return self.name
    

class BenchDistrict(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Местопроведения')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Ссылка')
    avatar = models.ImageField(default='default.png', upload_to='bench_district/', blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Местопроведения'
        verbose_name_plural = 'Местопроведения'

    def __str__(self):
        return self.name


class Bench(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название мероприятия')

    avatar = models.ImageField(default='default.png', upload_to='bench_avatars/', blank=True, null=True)

    created_date = models.DateTimeField(verbose_name='Дата и время')

    deskription = models.TextField(blank=True)

    type = models.ForeignKey(BenchType, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(BenchDistrict, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятие"

    def __str__(self):
        return str(self.id)
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        # Здесь вы можете вернуть путь к изображению по умолчанию или другую логику по вашему выбору
        return '/media/default.png'
