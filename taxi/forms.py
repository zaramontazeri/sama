from django import forms
from .models import Driver, DriverContract, Car, CarModel, Travel, Location, RegionRadius, RegionPolygon


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['national_code', 'driver_code', 'file_code', 'full_name', 'phones', 'avatar', 'active', 'online', 'licence_grade_code', 'email', 'rate', 'birthdate', 'gender', 'is_single', 'certificate_date', 'taxi_licnese_date', 'user']


class DriverContractForm(forms.ModelForm):
    class Meta:
        model = DriverContract
        fields = ['start_date', 'end_date', 'salari', 'salari_type', 'price_increase', 'driver']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'car_color', 'produce_year', 'technical_date', 'insurance_date', 'car_code', 'service_type', 'vin_number', 'chasis_number', 'motor_number', 'model', 'car']


class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'type']


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['name', 'source_address', 'source_point', 'destination_address', 'destination_point', 'pickup_time', 'dropoff_time', 'driver', 'car']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['point', 'speed']


class RegionRadiusForm(forms.ModelForm):
    class Meta:
        model = RegionRadius
        fields = ['point', 'radius', 'driver']


class RegionPolygonForm(forms.ModelForm):
    class Meta:
        model = RegionPolygon
        fields = ['polygon', 'Driver']


