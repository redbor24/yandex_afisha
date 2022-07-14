from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    features = []

    for place in Place.objects.all():
        features.append(get_place_description(place))

    geo_places = dict(
        type='FeatureCollection',
        features=features
    )
    context = {'places_geojson': geo_places}

    return render(request, 'index.html', context)


def get_place_description(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
        },
        'properties': {
            'title': place.title,
            'placeId': place.pk,
            'detailsUrl': reverse('places', args=[place.pk])
        }
    }


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    place_images = []

    for place_image in place.images.all():
        place_images.append(place_image.image.url)

    place_description = {
        'title': place.title,
        'imgs': place_images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(
        place_description,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )
