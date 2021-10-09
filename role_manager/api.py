from drf_yasg2.openapi import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework import viewsets, permissions
from role_manager import permissions as role_permissions

class ApiUrlViewSet(viewsets.ModelViewSet):
    """ViewSet for the ApiUrl class"""

    queryset = models.ApiUrl.objects.all()
    serializer_class = serializers.ApiUrlSerializer
    permission_classes = [permissions.IsAuthenticated,role_permissions.HasGroupRolePermission]


class ConsumerProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the ConsumerProject class"""

    queryset = models.ConsumerProject.objects.all()
    serializer_class = serializers.ConsumerProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComponentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Component class"""

    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer
    permission_classes = [permissions.IsAuthenticated]

class Test(APIView):
    permission_classes = [permissions.IsAuthenticated,role_permissions.HasGroupRolePermission]

    def get(self,request,*args,**kwargs):
        return Response({"status":"ok"})
