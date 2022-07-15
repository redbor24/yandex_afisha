from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html, mark_safe

from places.models import Image, Place


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'preview_image', 'num', )
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    extra = 0

    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        return format_html(
            '{}',
            mark_safe('<img src="{url}" height={height} />'.format(url=obj.image.url, height=200))
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )
    search_fields = ('title', )
    inlines = [ImagesInline]
    save_on_top = True