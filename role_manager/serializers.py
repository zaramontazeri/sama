from . import models

from rest_framework import serializers


class ApiUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ApiUrl
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'url', 
            'action', 
            'description', 
        )


class ConsumerProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ConsumerProject
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
        )


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Component
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
        )


