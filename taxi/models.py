from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.contrib.gis.db import models as models
from django_extensions.db import fields as extension_fields

class Driver(models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    national_code = models.CharField(max_length=12)
    driver_code = models.CharField(max_length=100)
    file_code = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    phones = ArrayField(models.CharField(max_length=100))
    avatar = models.ImageField(upload_to="upload/driver/")
    address = models.TextField(max_length=100)
    address_point = models.PointField(default=None,null=True,blank=True)
    active = models.BooleanField(default=True)
    online = models.BooleanField(default=False)
    licence_grade_code = models.CharField(max_length=30)
    email = models.EmailField(null=True,blank=True)
    rate = models.IntegerField(default=0)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6,choices=GENDER_TYPE)
    is_single = models.BooleanField(default=True)
    certificate_date = models.DateField()
    taxi_licnese_date = models.DateField()
    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="drivers", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk


class Car(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    car_color = models.CharField(max_length=30)
    produce_year = models.DateField()
    technical_date = models.DateField()
    insurance_date = models.DateField()
    car_code = models.CharField(max_length=30)
    service_type = models.CharField(max_length=30)
    vin_number = models.CharField(max_length=30)
    chasis_number = models.CharField(max_length=30)
    motor_number = models.CharField(max_length=30)

    # Relationship Fields
    model = models.ForeignKey(
        'taxi.CarModel',
        on_delete=models.CASCADE, related_name="cars", 
    )
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="cars", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug


class CarModel(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.TextField(max_length=100)
    passenger_cap = models.IntegerField()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug



class Travel(models.Model):
    REQUESTED = 'requested'
    STARTED = 'started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    STATUSES = (
        (REQUESTED, REQUESTED),
        (STARTED, STARTED),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED),
    )
    SCHOOL = 'school'
    TAXI_ONE_PASSENGER = 'one_passenger'
    TAXI_MANY_PASSENGER = 'many_passenger'
    SERVICE_TYPE = (
        (SCHOOL, SCHOOL),
        (TAXI_ONE_PASSENGER, TAXI_ONE_PASSENGER),
        (TAXI_MANY_PASSENGER, TAXI_MANY_PASSENGER),
    )
    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUSES, default=REQUESTED)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    source_address = models.TextField(max_length=100)
    source_point = models.PointField()
    destination_address = models.TextField(max_length=100)
    destination_point = models.PointField()
    pickup_time = models.DateTimeField()
    dropoff_time = models.DateTimeField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE, default=SCHOOL)
    
    # Relationship Fields
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="travels", 
    )
    car = models.ForeignKey(
        'taxi.Car',
        on_delete=models.CASCADE, related_name="travels", 
    )
    travelers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="travels", 
    )
    regions = models.ManyToManyField(
        "taxi.RegionPolygon",
        related_name="travels", 
    )
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug


class Location(models.Model):
    # Fields
    point = models.PointField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    speed = models.IntegerField()
    # Relationship Fields
    travel = models.ForeignKey(
        'taxi.Travel',
        on_delete=models.CASCADE, related_name="locations", null=True,blank=True
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk


class RegionRadius(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    point = models.PointField()
    radius = models.IntegerField()

    # Relationship Fields
    driver = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="regionradiuss", 
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk


class RegionPolygon(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    polygon = models.PolygonField()



    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

class TaxiSchedule(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    # Relationship Fields
    request = models.ForeignKey(
        'transportation_company.Request',
        on_delete=models.CASCADE, related_name="schdules", null=True,blank=True
    )

    contract = models.ForeignKey(
        'transportation_company.Contract',
        on_delete=models.CASCADE, related_name="schdules", null=True,blank=True
    )

    taxi = models.ForeignKey(
        'taxi.Driver',
        on_delete=models.CASCADE, related_name="schdules",
    )
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk
