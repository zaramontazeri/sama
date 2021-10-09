import unittest
from django.urls import reverse
from django.test import Client
from .models import Parent, Student, School
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_parent(**kwargs):
    defaults = {}
    defaults["full_name"] = "full_name"
    defaults["emergency_numbers"] = "emergency_numbers"
    defaults["national_code"] = "national_code"
    defaults["gender"] = "gender"
    defaults["address_point"] = "address_point"
    defaults["address"] = "address"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return Parent.objects.create(**defaults)


def create_student(**kwargs):
    defaults = {}
    defaults["full_name"] = "full_name"
    defaults["national_code"] = "national_code"
    defaults["gender"] = "gender"
    defaults["student_code"] = "student_code"
    defaults.update(**kwargs)
    if "parent" not in defaults:
        defaults["parent"] = create_parent()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    if "school" not in defaults:
        defaults["school"] = create_school()
    return Student.objects.create(**defaults)


def create_school(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["manager_full_name"] = "manager_full_name"
    defaults["phone_numbers"] = "phone_numbers"
    defaults["time_shifts"] = "time_shifts"
    defaults["manager_mobile"] = "manager_mobile"
    defaults["manager_national_number"] = "manager_national_number"
    defaults["working_time"] = "working_time"
    defaults["address"] = "address"
    defaults["address_point"] = "address_point"
    defaults["deputy_mobile"] = "deputy_mobile"
    defaults["deputy_full_name"] = "deputy_full_name"
    defaults["service_officer"] = "service_officer"
    defaults["avatar"] = "avatar"
    defaults["postal_code"] = "postal_code"
    defaults["student_count"] = "student_count"
    defaults.update(**kwargs)
    return School.objects.create(**defaults)


class ParentViewTest(unittest.TestCase):
    '''
    Tests for Parent
    '''
    def setUp(self):
        self.client = Client()

    def test_list_parent(self):
        url = reverse('school_parent_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_parent(self):
        url = reverse('school_parent_create')
        data = {
            "full_name": "full_name",
            "emergency_numbers": "emergency_numbers",
            "national_code": "national_code",
            "gender": "gender",
            "address_point": "address_point",
            "address": "address",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_parent(self):
        parent = create_parent()
        url = reverse('school_parent_detail', args=[parent.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_parent(self):
        parent = create_parent()
        data = {
            "full_name": "full_name",
            "emergency_numbers": "emergency_numbers",
            "national_code": "national_code",
            "gender": "gender",
            "address_point": "address_point",
            "address": "address",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('school_parent_update', args=[parent.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class StudentViewTest(unittest.TestCase):
    '''
    Tests for Student
    '''
    def setUp(self):
        self.client = Client()

    def test_list_student(self):
        url = reverse('school_student_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        url = reverse('school_student_create')
        data = {
            "full_name": "full_name",
            "national_code": "national_code",
            "gender": "gender",
            "student_code": "student_code",
            "parent": create_parent().pk,
            "user": create_django_contrib_auth_models_user().pk,
            "school": create_school().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_student(self):
        student = create_student()
        url = reverse('school_student_detail', args=[student.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_student(self):
        student = create_student()
        data = {
            "full_name": "full_name",
            "national_code": "national_code",
            "gender": "gender",
            "student_code": "student_code",
            "parent": create_parent().pk,
            "user": create_django_contrib_auth_models_user().pk,
            "school": create_school().pk,
        }
        url = reverse('school_student_update', args=[student.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SchoolViewTest(unittest.TestCase):
    '''
    Tests for School
    '''
    def setUp(self):
        self.client = Client()

    def test_list_school(self):
        url = reverse('school_school_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_school(self):
        url = reverse('school_school_create')
        data = {
            "name": "name",
            "manager_full_name": "manager_full_name",
            "phone_numbers": "phone_numbers",
            "time_shifts": "time_shifts",
            "manager_mobile": "manager_mobile",
            "manager_national_number": "manager_national_number",
            "working_time": "working_time",
            "address": "address",
            "address_point": "address_point",
            "deputy_mobile": "deputy_mobile",
            "deputy_full_name": "deputy_full_name",
            "service_officer": "service_officer",
            "avatar": "avatar",
            "postal_code": "postal_code",
            "student_count": "student_count",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_school(self):
        school = create_school()
        url = reverse('school_school_detail', args=[school.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_school(self):
        school = create_school()
        data = {
            "name": "name",
            "manager_full_name": "manager_full_name",
            "phone_numbers": "phone_numbers",
            "time_shifts": "time_shifts",
            "manager_mobile": "manager_mobile",
            "manager_national_number": "manager_national_number",
            "working_time": "working_time",
            "address": "address",
            "address_point": "address_point",
            "deputy_mobile": "deputy_mobile",
            "deputy_full_name": "deputy_full_name",
            "service_officer": "service_officer",
            "avatar": "avatar",
            "postal_code": "postal_code",
            "student_count": "student_count",
        }
        url = reverse('school_school_update', args=[school.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)