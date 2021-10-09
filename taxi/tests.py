import unittest
from django.urls import reverse
from django.test import Client
from .models import Driver, DriverContract, Car, CarModel, Travel, Location, RegionRadius, RegionPolygon
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_driver(**kwargs):
    defaults = {}
    defaults["national_code"] = "national_code"
    defaults["car_id"] = "car_id"
    defaults["driver_code"] = "driver_code"
    defaults["file_code"] = "file_code"
    defaults["full_name"] = "full_name"
    defaults["phones"] = "phones"
    defaults["avatar"] = "avatar"
    defaults["active"] = "active"
    defaults["online"] = "online"
    defaults["licence_grade_code"] = "licence_grade_code"
    defaults["email"] = "email"
    defaults["rate"] = "rate"
    defaults["birthdate"] = "birthdate"
    defaults["gender"] = "gender"
    defaults["is_single"] = "is_single"
    defaults["certificate_date"] = "certificate_date"
    defaults["taxi_licnese_date"] = "taxi_licnese_date"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Driver.objects.create(**defaults)


def create_drivercontract(**kwargs):
    defaults = {}
    defaults["start_date"] = "start_date"
    defaults["end_date"] = "end_date"
    defaults["salari"] = "salari"
    defaults["salari_type"] = "salari_type"
    defaults["price_increase"] = "price_increase"
    defaults.update(**kwargs)
    if "driver" not in defaults:
        defaults["driver"] = create_driver()
    return DriverContract.objects.create(**defaults)


def create_car(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["car_color"] = "car_color"
    defaults["produce_year"] = "produce_year"
    defaults["technical_date"] = "technical_date"
    defaults["insurance_date"] = "insurance_date"
    defaults["car_code"] = "car_code"
    defaults["service_type"] = "service_type"
    defaults["vin_number"] = "vin_number"
    defaults["chasis_number"] = "chasis_number"
    defaults["motor_number"] = "motor_number"
    defaults.update(**kwargs)
    if "model" not in defaults:
        defaults["model"] = create_carmodel()
    if "car" not in defaults:
        defaults["car"] = create_car()
    return Car.objects.create(**defaults)


def create_carmodel(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["type"] = "type"
    defaults.update(**kwargs)
    return CarModel.objects.create(**defaults)


def create_travel(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["source_address"] = "source_address"
    defaults["source_point"] = "source_point"
    defaults["destination_address"] = "destination_address"
    defaults["destination_point"] = "destination_point"
    defaults["pickup_time"] = "pickup_time"
    defaults["dropoff_time"] = "dropoff_time"
    defaults.update(**kwargs)
    if "driver" not in defaults:
        defaults["driver"] = create_driver()
    if "car" not in defaults:
        defaults["car"] = create_car()
    return Travel.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["point"] = "point"
    defaults["speed"] = "speed"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


def create_regionradius(**kwargs):
    defaults = {}
    defaults["point"] = "point"
    defaults["radius"] = "radius"
    defaults.update(**kwargs)
    if "driver" not in defaults:
        defaults["driver"] = create_driver()
    return RegionRadius.objects.create(**defaults)


def create_regionpolygon(**kwargs):
    defaults = {}
    defaults["polygon"] = "polygon"
    defaults.update(**kwargs)
    if "Driver" not in defaults:
        defaults["Driver"] = create_driver()
    return RegionPolygon.objects.create(**defaults)


class DriverViewTest(unittest.TestCase):
    '''
    Tests for Driver
    '''
    def setUp(self):
        self.client = Client()

    def test_list_driver(self):
        url = reverse('taxi_driver_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_driver(self):
        url = reverse('taxi_driver_create')
        data = {
            "national_code": "national_code",
            "car_id": "car_id",
            "driver_code": "driver_code",
            "file_code": "file_code",
            "full_name": "full_name",
            "phones": "phones",
            "avatar": "avatar",
            "active": "active",
            "online": "online",
            "licence_grade_code": "licence_grade_code",
            "email": "email",
            "rate": "rate",
            "birthdate": "birthdate",
            "gender": "gender",
            "is_single": "is_single",
            "certificate_date": "certificate_date",
            "taxi_licnese_date": "taxi_licnese_date",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_driver(self):
        driver = create_driver()
        url = reverse('taxi_driver_detail', args=[driver.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_driver(self):
        driver = create_driver()
        data = {
            "national_code": "national_code",
            "car_id": "car_id",
            "driver_code": "driver_code",
            "file_code": "file_code",
            "full_name": "full_name",
            "phones": "phones",
            "avatar": "avatar",
            "active": "active",
            "online": "online",
            "licence_grade_code": "licence_grade_code",
            "email": "email",
            "rate": "rate",
            "birthdate": "birthdate",
            "gender": "gender",
            "is_single": "is_single",
            "certificate_date": "certificate_date",
            "taxi_licnese_date": "taxi_licnese_date",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('taxi_driver_update', args=[driver.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DriverContractViewTest(unittest.TestCase):
    '''
    Tests for DriverContract
    '''
    def setUp(self):
        self.client = Client()

    def test_list_drivercontract(self):
        url = reverse('taxi_drivercontract_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_drivercontract(self):
        url = reverse('taxi_drivercontract_create')
        data = {
            "start_date": "start_date",
            "end_date": "end_date",
            "salari": "salari",
            "salari_type": "salari_type",
            "price_increase": "price_increase",
            "driver": create_driver().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_drivercontract(self):
        drivercontract = create_drivercontract()
        url = reverse('taxi_drivercontract_detail', args=[drivercontract.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_drivercontract(self):
        drivercontract = create_drivercontract()
        data = {
            "start_date": "start_date",
            "end_date": "end_date",
            "salari": "salari",
            "salari_type": "salari_type",
            "price_increase": "price_increase",
            "driver": create_driver().pk,
        }
        url = reverse('taxi_drivercontract_update', args=[drivercontract.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CarViewTest(unittest.TestCase):
    '''
    Tests for Car
    '''
    def setUp(self):
        self.client = Client()

    def test_list_car(self):
        url = reverse('taxi_car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_car(self):
        url = reverse('taxi_car_create')
        data = {
            "name": "name",
            "car_color": "car_color",
            "produce_year": "produce_year",
            "technical_date": "technical_date",
            "insurance_date": "insurance_date",
            "car_code": "car_code",
            "service_type": "service_type",
            "vin_number": "vin_number",
            "chasis_number": "chasis_number",
            "motor_number": "motor_number",
            "model": create_carmodel().pk,
            "car": create_car().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_car(self):
        car = create_car()
        url = reverse('taxi_car_detail', args=[car.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_car(self):
        car = create_car()
        data = {
            "name": "name",
            "car_color": "car_color",
            "produce_year": "produce_year",
            "technical_date": "technical_date",
            "insurance_date": "insurance_date",
            "car_code": "car_code",
            "service_type": "service_type",
            "vin_number": "vin_number",
            "chasis_number": "chasis_number",
            "motor_number": "motor_number",
            "model": create_carmodel().pk,
            "car": create_car().pk,
        }
        url = reverse('taxi_car_update', args=[car.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CarModelViewTest(unittest.TestCase):
    '''
    Tests for CarModel
    '''
    def setUp(self):
        self.client = Client()

    def test_list_carmodel(self):
        url = reverse('taxi_carmodel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_carmodel(self):
        url = reverse('taxi_carmodel_create')
        data = {
            "name": "name",
            "type": "type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_carmodel(self):
        carmodel = create_carmodel()
        url = reverse('taxi_carmodel_detail', args=[carmodel.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_carmodel(self):
        carmodel = create_carmodel()
        data = {
            "name": "name",
            "type": "type",
        }
        url = reverse('taxi_carmodel_update', args=[carmodel.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TravelViewTest(unittest.TestCase):
    '''
    Tests for Travel
    '''
    def setUp(self):
        self.client = Client()

    def test_list_travel(self):
        url = reverse('taxi_travel_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_travel(self):
        url = reverse('taxi_travel_create')
        data = {
            "name": "name",
            "source_address": "source_address",
            "source_point": "source_point",
            "destination_address": "destination_address",
            "destination_point": "destination_point",
            "pickup_time": "pickup_time",
            "dropoff_time": "dropoff_time",
            "driver": create_driver().pk,
            "car": create_car().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_travel(self):
        travel = create_travel()
        url = reverse('taxi_travel_detail', args=[travel.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_travel(self):
        travel = create_travel()
        data = {
            "name": "name",
            "source_address": "source_address",
            "source_point": "source_point",
            "destination_address": "destination_address",
            "destination_point": "destination_point",
            "pickup_time": "pickup_time",
            "dropoff_time": "dropoff_time",
            "driver": create_driver().pk,
            "car": create_car().pk,
        }
        url = reverse('taxi_travel_update', args=[travel.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''
    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('taxi_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('taxi_location_create')
        data = {
            "point": "point",
            "speed": "speed",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('taxi_location_detail', args=[location.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "point": "point",
            "speed": "speed",
        }
        url = reverse('taxi_location_update', args=[location.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RegionRadiusViewTest(unittest.TestCase):
    '''
    Tests for RegionRadius
    '''
    def setUp(self):
        self.client = Client()

    def test_list_regionradius(self):
        url = reverse('taxi_regionradius_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_regionradius(self):
        url = reverse('taxi_regionradius_create')
        data = {
            "point": "point",
            "radius": "radius",
            "driver": create_driver().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_regionradius(self):
        regionradius = create_regionradius()
        url = reverse('taxi_regionradius_detail', args=[regionradius.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_regionradius(self):
        regionradius = create_regionradius()
        data = {
            "point": "point",
            "radius": "radius",
            "driver": create_driver().pk,
        }
        url = reverse('taxi_regionradius_update', args=[regionradius.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RegionPolygonViewTest(unittest.TestCase):
    '''
    Tests for RegionPolygon
    '''
    def setUp(self):
        self.client = Client()

    def test_list_regionpolygon(self):
        url = reverse('taxi_regionpolygon_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_regionpolygon(self):
        url = reverse('taxi_regionpolygon_create')
        data = {
            "polygon": "polygon",
            "Driver": create_driver().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_regionpolygon(self):
        regionpolygon = create_regionpolygon()
        url = reverse('taxi_regionpolygon_detail', args=[regionpolygon.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_regionpolygon(self):
        regionpolygon = create_regionpolygon()
        data = {
            "polygon": "polygon",
            "Driver": create_driver().pk,
        }
        url = reverse('taxi_regionpolygon_update', args=[regionpolygon.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


