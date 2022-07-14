from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название локации', db_index=True, blank=False)
    description_short = models.CharField(max_length=255, verbose_name='Краткое описание', blank=False)
    description_long = models.TextField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта', null=False)
    lng = models.FloatField(verbose_name='Долгота', null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Image(models.Model):
    num = models.IntegerField(verbose_name='Порядковый номер изображения локации', null=False)
    image = models.ImageField(upload_to='', verbose_name='Изображение локации', null=True)
    place = models.ForeignKey(Place, verbose_name='Локация', on_delete=models.CASCADE, related_name='images',
                              db_index=True)

    def __str__(self):
        return f'{self.num} {self.place.title}'

    class Meta:
        verbose_name = 'Изображение локации'
        verbose_name_plural = 'Изображения локации'
