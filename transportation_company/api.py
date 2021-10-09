from rest_framework.generics import ListAPIView
from . import models
from . import serializers
from rest_framework import viewsets, permissions


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverContractViewSet(viewsets.ModelViewSet):
    """ViewSet for the DriverContract class"""

    queryset = models.DriverContract.objects.all()
    serializer_class = serializers.DriverContractSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContractViewSet(viewsets.ModelViewSet):
    """ViewSet for the Contract class"""

    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressViewSet(viewsets.ModelViewSet):
    """ViewSet for the Address class"""

    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstallmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Installment class"""

    queryset = models.Installment.objects.all()
    serializer_class = serializers.InstallmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstallmentChequeViewSet(viewsets.ModelViewSet):
    """ViewSet for the InstallmentCheque class"""

    queryset = models.InstallmentCheque.objects.all()
    serializer_class = serializers.InstallmentChequeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequestViewSet(viewsets.ModelViewSet):
    """ViewSet for the Request class"""

    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudentRequestListApiView(ListAPIView):
    queryset = models.StudentRequest.objects.all()
    serializer_class = serializers.StudentRequestSerializer

class StudentPeriodRequestListApiView(ListAPIView):
    queryset = models.StudentPeriodRequest.objects.all()
    serializer_class = serializers.StudentPeriodRequestSerializer

class UserRequestListApiView(ListAPIView):
    queryset = models.UserRequest.objects.all()
    serializer_class = serializers.UserRequestSerializer