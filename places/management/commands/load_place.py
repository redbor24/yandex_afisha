import json
import os
from urllib.parse import unquote, urlsplit

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


def create_place(place_url):
    response = requests.get(place_url)
    response.raise_for_status()

    try:
        place_descr = response.json()
    except json.decoder.JSONDecodeError:
        print('Ошибка формата GeoJson.')
        return

    coordinates = place_descr.get('coordinates')

    place, is_new_place = Place.objects.get_or_create(
        title=place_descr.get('title'),
        defaults={
            'description_short': place_descr.get('description_short'),
            'description_long': place_descr.get('description_long'),
            'lat': coordinates.get('lat'),
            'lng': coordinates.get('lng')
        }
    )

    if is_new_place:
        place_images_urls = place_descr.get('imgs')
        download_place_images(place, place_images_urls)


def download_place_images(place, image_urls):
    for image_url in image_urls:
        response = requests.get(image_url)
        response.raise_for_status()

        image_filename = os.path.basename(unquote(urlsplit(image_url).path))

        image_content = ContentFile(response.content)

        place_image = Image(places=place)
        place_image.num = place.images.count() + 1
        place_image.image.save(image_filename, image_content, save=True)
        place_image.save()


class Command(BaseCommand):
    help = 'Load place from GeoJSON.'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        if options['place_url']:
            create_place(options['place_url'])
