from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название локации', db_index=True)
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lng = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        unique_together = ['title', 'lat', 'lng']
        ordering = ['id', 'title']


class Image(models.Model):
    num = models.IntegerField(verbose_name='Порядковый номер изображения локации', default=1)
    image = models.ImageField(verbose_name='Изображение локации')
    places = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.CASCADE, related_name='images',
                               db_index=True)

    def __str__(self):
        return f'{self.num} {self.places.title}'

    class Meta:
        verbose_name = 'Изображение локации'
        verbose_name_plural = 'Изображения локации'
        ordering = ['num']
