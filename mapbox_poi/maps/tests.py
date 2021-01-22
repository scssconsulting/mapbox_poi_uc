from django.test import TestCase
from django.urls import reverse

from maps.models import POI


class MapViewTests(TestCase):
    def test_general(self):
        response = self.client.get(reverse('maps:map_view'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['pois'], POI.objects.filter(status=True))
        self.assertEqual(len(response.context['geometries']['features']),
                         len(POI.objects.filter(status=True, geometry__isnull=False)))
