from django.urls import path, include
from rest_framework import routers

from . import api

router = routers.DefaultRouter()
router.register(r'company', api.CompanyViewSet)
router.register(r'contract', api.ContractViewSet)
router.register(r'address', api.AddressViewSet)
router.register(r'installment', api.InstallmentViewSet)
router.register(r'installmentcheque', api.InstallmentChequeViewSet)
router.register(r'request', api.RequestViewSet)
router.register(r'drivercontract', api.DriverContractViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    path("userrequest",api.UserRequestListApiView.as_view()),
    path("studentperiodrequest",api.StudentPeriodRequestListApiView.as_view()),
    path("studentrequest",api.StudentRequestListApiView.as_view())

)