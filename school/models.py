from django.db.models.fields import BLANK_CHOICE_DASH, CharField, IntegerField, TextField
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.contrib.gis.db import models as models


class Parent(models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    full_name = models.CharField(max_length=100)
    emergency_numbers = ArrayField(models.CharField(max_length=100))
    national_code = models.CharField(max_length=10)
    gender = models.CharField(max_length=6,choices=GENDER_TYPE)
    address_point = models.PointField()
    address = JSONField(default=dict)

    # Relationship Fields
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s : %s' % (self.full_name ,self.national_code)

    def get_absolute_url(self):
        return reverse('school_parent_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('school_parent_update', args=(self.pk,))


class Student(models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    full_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=12)
    gender = models.CharField(max_length=8,choices=GENDER_TYPE)
    student_code = models.CharField(max_length=30,default=0)

    # Relationship Fields
    parent = models.ForeignKey(
        'school.Parent',
        on_delete=models.CASCADE, related_name="children"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="student",null=True,blank=True
    )
    school = models.ForeignKey(
        'school.School',
        on_delete=models.CASCADE, related_name="students", null=True,blank=True
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('school_student_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('school_student_update', args=(self.pk,))

class City(models.Model):
    # Fields
    name = models.CharField(max_length=255)

class Region(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    # Relationship Fields
    city = models.ForeignKey(
        'school.City',
        on_delete=models.CASCADE, related_name="regions"
    )
    def __unicode__(self):
        return u'%s - %s' % (self.name ,self.city.name)

class Level(models.Model):
    FEMALE= "female"
    MALE ="male"
    GENDER_TYPE = ((FEMALE,'female'),(MALE,"male"))
    # Fields
    level = CharField(max_length=20)
    part = CharField(max_length=30,null=True,blank=True)
    gender = CharField(max_length=10 ,choices=GENDER_TYPE,null=True,blank=True)
    working_time = JSONField(default=dict,null=True,blank=True)

class School(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manager_full_name = models.CharField(max_length=30)
    phone_numbers = ArrayField(models.CharField(max_length=100))
    manager_mobile = models.CharField(max_length=30)
    manager_national_number = models.TextField(max_length=100)
    address = TextField(default=dict)
    address_point = models.PointField()
    deputy_mobile = models.CharField(max_length=30)
    deputy_full_name = models.CharField(max_length=30)
    service_officer = JSONField(default=dict, null=True,blank=True)
    avatar = models.ImageField(max_length=100, null=True,blank=True)
    postal_code = models.TextField(max_length=100)
    student_count = models.IntegerField()
    city = models.CharField(max_length=20)
    # Relationship Fields
    # region = models.ForeignKey(
    #     'school.Region',
    #     on_delete=models.CASCADE, related_name="schools",null=True, blank=True
    # )
    levels = models.ManyToManyField('school.Level',related_name="schools")
    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('school_school_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('school_school_update', args=(self.pk,))
