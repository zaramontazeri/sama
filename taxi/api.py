from django.urls.conf import include, path
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView

from perian_tools.province.city import cities_key, city_details_by_key, city_location_by_key
from perian_tools.province.district import districts_key, search_by_fa_key, towns_list_by_district_key

from . import models
from . import serializers
from rest_framework import schemas, viewsets, permissions
from drf_yasg2.generators import SchemaGenerator
from rest_framework.response import Response
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.schemas.openapi import AutoSchema
from role_manager import permissions as role_permissions
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import  F
from django.contrib.gis.db.models.functions import Distance
from school import models as school_models
class DriverViewSet(viewsets.ModelViewSet):
    """ViewSet for the Driver class"""

    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    """ViewSet for the Car class"""

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarModelViewSet(viewsets.ModelViewSet):
    """ViewSet for the CarModel class"""

    queryset = models.CarModel.objects.all()
    serializer_class = serializers.CarModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class TravelViewSet(viewsets.ModelViewSet):
    """ViewSet for the Travel class"""

    queryset = models.Travel.objects.all()
    serializer_class = serializers.TravelSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Location class"""

    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegionRadiusViewSet(viewsets.ModelViewSet):
    """ViewSet for the RegionRadius class"""

    queryset = models.RegionRadius.objects.all()
    serializer_class = serializers.RegionRadiusSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        longitude = self.request.query_params.get('longitude',None)
        latitude= self.request.query_params.get('latitude',None)
        queryset = self.queryset
        if longitude and latitude:
            location = Point(float(longitude), float(latitude),srid=4326)
            # queryset = queryset.annotate(distance=Distance('regionradiuss__point', location))
            queryset = queryset.annotate(distance=Distance('point', location, srid=4326)).filter(distance__lte=F('radius')*1000)

        return queryset


class StudentRequestDriverListApiView(GenericAPIView):
    """ViewSet for the RegionRadius class"""

    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # longitude = self.request.query_params.get('longitude',None)
        # latitude= self.request.query_params.get('latitude',None)
        queryset = self.queryset
        data = self.request.data
        student_list = data.get("student_list",[])
        vip = data.get("vip",False)
        student = None
        parents = []
        genders = []
        #check students parent is same
        if len(student_list) == 0 :
            pass
        for st_id in student_list:
            student = school_models.Student.objects.get(id=st_id)
            parents.add(student.parent)
            genders.add(student.gender)
        
        parents = set(parents)
        genders = set(genders)
        if len(parents) != 1 or (len(genders)!=1 and vip == False):
            #raise error
            pass
        else :
            parent = parents[0]
        location = parent.address_point
        gender = student.gender
        region_queryset = models.RegionRadius.objects.all()
        region_ids = region_queryset.annotate(distance=Distance('point', location, srid=4326))\
            .filter(distance__lte=F('radius')*1000)\
            .values_list('id', flat=True)
        # queryset = queryset.filter(regionid__in = regi)
        # if longitude and latitude:
            # location = Point(float(longitude), float(latitude),srid=4326)
            # queryset = queryset.annotate(distance=Distance('regionradiuss__point', location))
            # region_ids = region_queryset.annotate(distance=Distance('point', location, srid=4326))\
            #     .filter(distance__lte=F('radius')*1000)\
            #     .values_list('id', flat=True)
        return queryset
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            drivers = [q.driver for q in page]
            serializer = self.get_serializer(drivers, many=True)
            return self.get_paginated_response(serializer.data)
        drivers = [q.driver for q in queryset]
        serializer = self.get_serializer(drivers, many=True)
        return Response(serializer.data)

class RegionPolygonViewSet(viewsets.ModelViewSet):
    """ViewSet for the RegionPolygon class"""
    queryset = models.RegionPolygon.objects.all()
    serializer_class = serializers.RegionPolygonSerializer
    permission_classes = [permissions.AllowAny]

class CityList(APIView):
    def get (self,request):
        cities = cities_key()
# Locations
        
        location = city_location_by_key("ZAHEDAN")
        print('**********')
        print("key" + ' : ')
        print(location)

        # Details => fa_key (persian object key)
 
        detail = city_details_by_key("ZAHEDAN")
        print(detail)

            # print('**********')
            # print(key + ' : ')
            # print(detail)

        # for key in fa_keys:
        #     locations = search_by_fa_key(key)
        #     print(locations)
            # print(key)
        town = towns_list_by_district_key("سیستان و بلوچستان")
        print(town)
        # print(towns)

        return Response(town)

# from rest_framework.schemas.openapi import AutoSchema
class SchemaView(APIView):
    permission_classes = [role_permissions.HasGroupRolePermission,permissions.AllowAny]
    # action = "schema_get"
    def get(self, request,a):
        generator = SchemaGenerator(
            title="RDMO API",
            # patterns=urlpatterns,
            # url=request.path
        )
        schema = generator.get_schema()
        endpoints = generator.endpoints
        # print(schema)
        # print (request.path)
        return Response({"s":"o"}) 


