from django.conf import settings


def mapbox(request):
    return {
        'MAPBOX_KEY': settings.MAPBOX_KEY
    }
