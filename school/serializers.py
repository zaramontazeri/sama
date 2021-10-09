from django.contrib.auth.password_validation import validate_password
from drf_extra_fields.fields import Base64ImageField
from . import models
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from django.contrib.auth.models import  Group

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from media_app.serializers import ImageRelatedField,FileRelatedField
from drf_extra_fields.geo_fields import PointField
# from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from auth_rest_phone import serializers as auth_serializers
from auth_rest_phone.conf import settings
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class ParentSerializer(serializers.ModelSerializer):
    address_point = PointField()
    class Meta:
        model = models.Parent
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'full_name', 
            'emergency_numbers', 
            'national_code', 
            'gender', 
            'address_point', 
            'address', 
            'user'
        )


class StudentUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }
    avatar = Base64ImageField(required=False)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password", "email", "first_name", "last_name", "avatar"
        )
       
    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            print(self.context,validated_data)
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            try:
                gr, cr = Group.objects.get_or_create(name=self.context["groups"])
                gr.user_set.add(user)
            except Exception as e:
                pass #group does not exist in context
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user

class StudentUserCreatePasswordRetypeSerializer(StudentUserCreateSerializer):     
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password", "email", "first_name", "last_name", "avatar"
        ) 
        extra_kwargs = {
            're_password': {'write_only': True},
        }  
    default_error_messages = {
        "password_mismatch": settings.CONSTANTS.messages.PASSWORD_MISMATCH_ERROR
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["re_password"] = serializers.CharField(
            style={"input_type": "password"}
        )

    def to_representation(self, instance):
        self.fields.pop('re_password',None)
        return super().to_representation(instance)

    def validate(self, attrs):
        self.fields.pop("re_password", None)
        re_password = attrs.pop("re_password")
        attrs = super().validate(attrs)
        if attrs["password"] == re_password:
            return attrs
        else:
            self.fail("password_mismatch")
            
class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = ("pk", "level" ,"part" ,"gender" ,"working_time") 

class RegionSerializer(serializers.ModelSerializer):
    # city = PresentablePrimaryKeyRelatedField(
    #     queryset=models.City.objects.all(),
    #     # presentation_serializer=CitySerializer,
    #     read_source=None,
    # )
    class Meta:
        model = models.Region
        fields =("pk","name","number")

class SchoolSerializer(serializers.ModelSerializer):
    levels = PresentablePrimaryKeyRelatedField(
        queryset=models.Level.objects.all(),
        presentation_serializer=LevelSerializer,
        read_source=None,
        many=True
    )
    region=PresentablePrimaryKeyRelatedField(
        queryset=models.Region.objects.all(),
        presentation_serializer=RegionSerializer,
        read_source=None,
    )
    address_point=PointField()
    class Meta:
        model = models.School
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'manager_full_name', 
            'phone_numbers', 
            'manager_mobile', 
            'manager_national_number', 
            'address', 
            'address_point', 
            'deputy_mobile', 
            'deputy_full_name', 
            'service_officer', 
            'avatar', 
            'postal_code', 
            'student_count', 
            'region',
            'levels'
        )


class StudentSerializer(WritableNestedModelSerializer):
    parent = PresentablePrimaryKeyRelatedField(
        queryset=models.Parent.objects.all(),
        presentation_serializer=ParentSerializer,
        read_source=None,
    )
    school = PresentablePrimaryKeyRelatedField(
        queryset=models.School.objects.all(),
        presentation_serializer=SchoolSerializer,
        read_source=None,
    )
    # user = User
    class Meta:
        model = models.Student
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'full_name', 
            'national_code', 
            'gender', 
            'student_code', 
            'parent',
            'user',
            'school'
        )

# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.City
#         fields = "__all__"





