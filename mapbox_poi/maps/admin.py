from django.contrib import admin

from mapbox_location_field.admin import MapAdmin

from maps.models import POI, POICategory

admin.site.register(POICategory)
admin.site.register(POI, MapAdmin)
