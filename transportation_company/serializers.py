from . import models

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from media_app.serializers import ImageRelatedField,FileRelatedField
from drf_extra_fields.geo_fields import PointField
# from drf_extra_fields.fields import Base64ImageField
from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from auth_rest_phone import serializers as auth_serializers
from rest_polymorphic.serializers import PolymorphicSerializer

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            'pk', 
            'name', 
            'created', 
            'last_updated', 
            'point', 
            'address', 
        )

class CompanySerializer(WritableNestedModelSerializer):
    addresses = AddressSerializer(many=True)
    class Meta:
        model = models.Company
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'manager_full_name', 
            'manager_national_code', 
            'name', 
            'avatar', 
            'email', 
            'website', 
            'active', 
            'phone_numbers', 
            'capacity', 
            'service_types', 
            'files',
            'addresses'
        )

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contract
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'status', 
            'service_type', 
            'commission_rate_contract', 
            'source_loc', 
            'destination_loc', 
            'source_address', 
            'destination_address', 
            'side_way', 
            'special', 
            'company',
            "sweep_time",
            "return_time" 
        )


class DriverContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DriverContract
        fields = (
            'pk', 
            'created', 
            'last_updated', 
            'start_date', 
            'end_date', 
            'salari', 
            'salari_type', 
            'price_increase', 
            'driver',
            'company'
        )

class StudentContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentContract
        fields = "__all__"

class ContractPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'contract_type'
    model_serializer_mapping = {
        models.Contract: ContractSerializer,
        models.StudentContract: StudentContractSerializer,
    }
    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()
class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Installment
        fields = (
            'pk',
            'created', 
            'last_updated', 
            'amount', 
            'status', 
            'pay_type', 
            'description', 
            'cheque_count', 
            'contract' 
    )
        


class InstallmentChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InstallmentCheque
        fields = (
            'pk',
            'cheque_number', 
            'created', 
            'last_updated', 
            'bank_name', 
            'track_card_payment_number', 
            'description', 
            'state', 
            'due_date', 
            'amount', 
        )

class StudentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentRequest
        fields = "__all__"

class StudentPeriodRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentPeriodRequest
        fields = "__all__"

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRequest
        fields = "__all__"

class RequestPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = 'request_type'
    model_serializer_mapping = {
        models.StudentRequest: StudentRequestSerializer,
        models.StudentPeriodRequest: StudentPeriodRequestSerializer,
        models.UserRequest:UserRequestSerializer
    }
    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()