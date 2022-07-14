from django.utils.html import format_html, mark_safe
from django.contrib import admin
from places.models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    fields = ('image', 'preview_image', 'num', )
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    extra = 0

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html(
            '{}',
            mark_safe(
                '<img src="{url}" height={height} />'.format(
                    url=obj.image.url,
                    height=200,
                )
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
