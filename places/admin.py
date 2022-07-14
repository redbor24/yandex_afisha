from django.contrib import admin
from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    fields = ('image', 'num', )
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
