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
