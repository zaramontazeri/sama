from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'driver', api.DriverViewSet)
router.register(r'car', api.CarViewSet)
router.register(r'carmodel', api.CarModelViewSet)
router.register(r'travel', api.TravelViewSet)
router.register(r'location', api.LocationViewSet)
router.register(r'regionradius', api.RegionRadiusViewSet)
router.register(r'regionpolygon', api.RegionPolygonViewSet)
urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    path("schema/<str:a>/",api.SchemaView.as_view(),name="schema"),
    path("avail_drivers/",api.StudentRequestDriverListApiView.as_view(),name="driver_region"),
    path("cities/",api.CityList.as_view(),name="cities")

)