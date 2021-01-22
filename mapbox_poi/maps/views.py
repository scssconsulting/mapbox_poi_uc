from django.shortcuts import render

from maps.models import POI


def map_view(request):
    """
    Basic view to send POI and Geometries to frontend
    """
    pois = POI.objects.filter(status=True)
    geometries = {'type': 'FeatureCollection', 'features': [i.geometry for i in pois.filter(geometry__isnull=False)]}
    return render(request, 'default.html', {'pois': pois, 'geometries': geometries})
