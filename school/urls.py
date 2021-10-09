from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'parent', api.ParentViewSet)
router.register(r'student', api.StudentViewSet)
router.register(r'school', api.SchoolViewSet)
# router.register(r'city', api.CityViewSet)
router.register(r'region', api.RegionViewSet)
router.register(r'level', api.LevelViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
)