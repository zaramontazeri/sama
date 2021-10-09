from django.contrib.gis import admin
from django import forms
from .models import Driver, Car, CarModel, Travel, Location, RegionRadius, RegionPolygon

class DriverAdminForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = '__all__'


class DriverAdmin(admin.OSMGeoAdmin):
    form = DriverAdminForm
    list_display = ['created', 'last_updated']

admin.site.register(Driver, DriverAdmin)

class CarAdminForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'


class CarAdmin(admin.ModelAdmin):
    form = CarAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'car_color', 'produce_year', 'technical_date', 'insurance_date', 'car_code', 'service_type', 'vin_number', 'chasis_number', 'motor_number']
    readonly_fields = [ 'created', 'last_updated']

admin.site.register(Car, CarAdmin)


class CarModelAdminForm(forms.ModelForm):

    class Meta:
        model = CarModel
        fields = '__all__'


class CarModelAdmin(admin.ModelAdmin):
    form = CarModelAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'type']
    readonly_fields = [ 'created', 'last_updated']

admin.site.register(CarModel, CarModelAdmin)


class TravelAdminForm(forms.ModelForm):

    class Meta:
        model = Travel
        fields = '__all__'


class TravelAdmin(admin.OSMGeoAdmin):
    form = TravelAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'source_address', 'source_point', 'destination_address', 'destination_point', 'pickup_time', 'dropoff_time']
    readonly_fields = [ 'created', 'last_updated']

admin.site.register(Travel, TravelAdmin)


class LocationAdminForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'


class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['point', 'created', 'last_updated', 'speed']
    readonly_fields = [ 'created', 'last_updated']

admin.site.register(Location, LocationAdmin)


class RegionRadiusAdminForm(forms.ModelForm):

    class Meta:
        model = RegionRadius
        fields = '__all__'


class RegionRadiusAdmin(admin.OSMGeoAdmin):
    form = RegionRadiusAdminForm
    list_display = ['created', 'last_updated',]
    readonly_fields = ['created', 'last_updated']

admin.site.register(RegionRadius, RegionRadiusAdmin)


class RegionPolygonAdminForm(forms.ModelForm):

    class Meta:
        model = RegionPolygon
        fields = '__all__'


class RegionPolygonAdmin(admin.OSMGeoAdmin):
    form = RegionPolygonAdminForm
    list_display = ['created', 'last_updated', 'polygon']
    readonly_fields = ['created', 'last_updated']

admin.site.register(RegionPolygon, RegionPolygonAdmin)


