from django.urls import reverse
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.contrib.gis.db import models as models
from django.contrib.postgres.fields import ArrayField
from polymorphic.models import PolymorphicModel

class Company(models.Model):
    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manager_full_name = models.CharField(max_length=30)
    manager_national_code = models.CharField(max_length=12)
    avatar = models.ImageField(upload_to="upload/company/",null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    active = models.BooleanField(default=True)
    phone_numbers = ArrayField(models.CharField(max_length=100,blank=True,null=True))
    capacity = models.IntegerField(default=0)
    service_types = models.JSONField(default=dict,null=True,blank=True)
    files = models.FileField(upload_to="upload/company_files/",null=True,blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

class Contract(PolymorphicModel):
    BOTH ="both"
    SOURCE ="source"
    DESTINATION = 'destination'
    SIDE_WAY =(
        (BOTH,"both"),
        (SOURCE,"source"),
        (DESTINATION , 'destination')
    )
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.TextField(max_length=100)
    service_type = models.CharField(max_length=30)
    commission_rate_contract = models.IntegerField()
    source_loc = models.PointField()
    destination_loc = models.PointField()
    source_address = models.TextField(max_length=100)
    destination_address = models.TextField(max_length=100)
    side_way = models.CharField(max_length=12,choices=SIDE_WAY)
    special = models.BooleanField(default=False)
    period = models.IntegerField(default=5)
    sweep_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True,blank=True)
    # Relationship Fields
    company = models.ForeignKey(
        'transportation_company.Company',
        on_delete=models.CASCADE, related_name="contract", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

class StudentContract(Contract):
    # Relationship Fields
    parent = models.ForeignKey(
        'school.Parent',
        on_delete=models.CASCADE, related_name="contracts", 
    )
    student = models.ForeignKey(
        'school.Student',
        on_delete=models.CASCADE, related_name="contracts", 
    )


class DriverContract(models.Model):
    MONTHLY='monthly'
    YEARLY='yearly'
    DAILY='daily'
    PER_TRAVEL='travel'

    SALARY_TYPE =((MONTHLY,'monthly'),
    (YEARLY,'yearly'),
    (DAILY,'daily'),
    (PER_TRAVEL,'travel')
    )
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    salari = models.IntegerField()
    salari_type = models.CharField(max_length=30,choices=SALARY_TYPE)
    price_increase = models.JSONField(null=True,blank=True)
    vip = models.BooleanField(default=False)

    # Relationship Fields
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="drivercontracts", 
    )
    company = models.ForeignKey(
        'transportation_company.Company',
        on_delete=models.CASCADE, related_name="drivercontracts", 
    )
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk


class Address(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    point = models.PointField()
    address = models.TextField(max_length=100)
    
    # Relationship Fields
    company = models.ForeignKey(
        'transportation_company.Company',
        on_delete=models.CASCADE, related_name="addresses", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk


class Installment(models.Model):
    PENDING ="pending"
    PAYED ="pass"
    CASHE = 'cashe'
    INSTALLMENT = 'installment'
    INSTALLMENT_STATE =(
        (PENDING,"pending"),
        (PAYED,"payed")
    )
    PAY_TYPE =(
        (CASHE,"cashe"),
        (INSTALLMENT,"installment")
    )
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    amount = models.DecimalField(max_digits=20, decimal_places=0)
    status = models.CharField(max_length=8,choices=INSTALLMENT_STATE,default='pending')
    pay_type = models.CharField(max_length=100,choices=PAY_TYPE,default='cashe')
    description = models.TextField(max_length=100)
    cheque_count = models.IntegerField(default=0)
    # Relationship Fields
    contract = models.OneToOneField(
        'transportation_company.Installment',
        on_delete=models.CASCADE, related_name="installments", 
    )
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug

class InstallmentCheque(models.Model):
    REJECTED ="reject"
    PASSED ="pass"
    EXPIRED  = 'expired'
    CEHQUE_STATE =(
        (REJECTED,"rejected"),
        (PASSED,"passed"),
        (EXPIRED ,"expired")
    )
    # Fields
    cheque_number = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    bank_name = models.CharField(max_length=30)
    track_card_payment_number = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    state = models.CharField(max_length=8,choices=CEHQUE_STATE)
    due_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=20, decimal_places=0)

    # Relationship Fields
    installment = models.ForeignKey(
        'transportation_company.Installment',
        on_delete=models.CASCADE, related_name="installmentcheques", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug


class Request(PolymorphicModel):
    BOTH ="both"
    SOURCE ="source"
    DESTINATION = 'destination'
    SIDE_WAY =(
        (BOTH,"both"),
        (SOURCE,"source"),
        (DESTINATION , 'destination')
    )
    SINGLE = 'single_pass'
    MULTIPLE = 'multiple_pass'
    SERVICE = 'service'

    SERVICE_TYPE =(
        (SINGLE,"single"),
        (MULTIPLE,"multiple"),
        (SERVICE,"service")
    )
    PENDING ="pending"
    APPROVED = "approved"

    STATUS =(
        (PENDING,"pending"),
        (APPROVED,"approved"),
    )
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=20,choices=STATUS,default="pending")
    service_type = models.CharField(max_length=20,choices=SERVICE_TYPE,default="service")
    commission_rate_contract = models.IntegerField()
    source_loc = models.PointField()
    destination_loc = models.PointField()
    source_address = models.TextField(max_length=100)
    destination_address = models.TextField(max_length=100)
    side_way = models.CharField(max_length=12,choices=SIDE_WAY)
    special = models.BooleanField(default=False)
    sweep_time = models.DateTimeField()
    return_time = models.DateTimeField(null=True,blank=True)
    vip = models.BooleanField(default=False)
    # Relationship Fields
    installment = models.OneToOneField(
        'transportation_company.Installment',
        on_delete=models.CASCADE, related_name="requests", 
    )
    company = models.ForeignKey(
        'transportation_company.Company',
        on_delete=models.CASCADE, related_name="requests", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

class StudentRequest(Request):

    # Relationship Fields
    parent = models.ForeignKey(
        'school.Parent',
        on_delete=models.CASCADE, related_name="student_requests", 
    )
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="student_requests", 
        null=True , blank=True
    )

class StudentPeriodRequest(Request):

    # Relationship Fields
    parent = models.ForeignKey(
        'school.Parent',
        on_delete=models.CASCADE, related_name="student_period_requests", 
    )
    contract =  models.ForeignKey(
        'transportation_company.Contract',
        on_delete=models.CASCADE, related_name="student_period_requests", 
        null=True , blank=True
    )
    period = models.IntegerField(default=5)

class UserRequest(Request):

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="user_requests", 
    )
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="user_requests", 
        null=True , blank=True
    )
