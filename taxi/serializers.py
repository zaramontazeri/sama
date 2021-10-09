from . import models

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from media_app.serializers import ImageRelatedField,FileRelatedField
from drf_extra_fields.geo_fields import PointField
from .serializer_fields import PolygonField
from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from auth_rest_phone import serializers as auth_serializers

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CarModel
        fields = (
            'pk',
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'type', 
            'passenger_cap'
        )

class CarSerializer(WritableNestedModelSerializer):
    model=CarModelSerializer()
    class Meta:
        model = models.Car
        fields = (
            'pk',
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'car_color', 
            'produce_year', 
            'technical_date', 
            'insurance_date', 
            'car_code', 
            'service_type', 
            'vin_number', 
            'chasis_number', 
            'motor_number', 
            'model',
            'driver'
        )


class DriverSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField()
    address_point = PointField()
    cars = CarSerializer(many=True)
    class Meta:
        model = models.Driver
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'national_code', 
            'driver_code', 
            'file_code', 
            'full_name', 
            'address',
            'address_point',
            'phones', 
            'avatar', 
            'active', 
            'online', 
            'licence_grade_code', 
            'email', 
            'rate', 
            'birthdate', 
            'gender', 
            'is_single', 
            'certificate_date', 
            'taxi_licnese_date', 
            'user',
            'cars'
        )




class TravelSerializer(serializers.ModelSerializer):
    source_point=PointField()
    destination_point=PointField()
    class Meta:
        model = models.Travel
        fields = (
            'pk',
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'source_address', 
            'source_point', 
            'destination_address', 
            'destination_point', 
            'pickup_time', 
            'dropoff_time', 
            'car',
            'driver',
            'travelers'
        )


class LocationSerializer(serializers.ModelSerializer):
    point = PointField()
    class Meta:
        model = models.Location
        fields = (
            'pk', 
            'point', 
            'created', 
            'last_updated', 
            'speed', 
            'travel'
        )


class RegionRadiusSerializer(serializers.ModelSerializer):
    point=PointField()
    class Meta:
        model = models.RegionRadius
        fields = (
            'pk', 
            # 'created', 
            # 'last_updated', 
            'point', 
            'radius', 
            'driver'
        )


class RegionPolygonSerializer(serializers.ModelSerializer):
    polygon = PolygonField()
    class Meta:
        model = models.RegionPolygon
        fields = (
            'pk',
            'name',
            'created', 
            'last_updated', 
            'polygon', 
        )


