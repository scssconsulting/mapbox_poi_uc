from django.db import models

from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class POICategory(models.Model):
    """
    Category for POI
    Make it dynamic so that easily maintainable by admin
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'POI Categories'


class POI(models.Model):
    """
    Persistent store for Point of Interest
    It can be anything from your favorite pub to favorite city. 
    """
    location = LocationField()
    name = AddressAutoHiddenField()
    category = models.ManyToManyField(POICategory, blank=True, default="What category your POI falls into")
    geometry = models.JSONField(null=True, blank=True)
    status = models.BooleanField(default=True, help_text="Only shown in the frontend if status is checked.")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'POI'