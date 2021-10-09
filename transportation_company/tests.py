import unittest
from django.urls import reverse
from django.test import Client
from .models import Company, Contract, Address, Installment, InstallmentCheque
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


def create_company(**kwargs):
    defaults = {}
    defaults["manager_full_name"] = "manager_full_name"
    defaults["manager_national_code"] = "manager_national_code"
    defaults["name"] = "name"
    defaults["avatar"] = "avatar"
    defaults["email"] = "email"
    defaults["website"] = "website"
    defaults["active"] = "active"
    defaults["phone_numbers"] = "phone_numbers"
    defaults["capacity"] = "capacity"
    defaults["service_types"] = "service_types"
    defaults.update(**kwargs)
    return Company.objects.create(**defaults)


def create_contract(**kwargs):
    defaults = {}
    defaults["status"] = "status"
    defaults["service_type"] = "service_type"
    defaults["commission_rate_contract"] = "commission_rate_contract"
    defaults["source_loc"] = "source_loc"
    defaults["destination_loc"] = "destination_loc"
    defaults["source_address"] = "source_address"
    defaults["destination_address"] = "destination_address"
    defaults["side_way"] = "side_way"
    defaults["special"] = "special"
    defaults.update(**kwargs)
    if "installment" not in defaults:
        defaults["installment"] = create_installment()
    return Contract.objects.create(**defaults)


def create_address(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["point"] = "point"
    defaults["address"] = "address"
    defaults.update(**kwargs)
    return Address.objects.create(**defaults)


def create_installment(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["amount"] = "amount"
    defaults["status"] = "status"
    defaults["pay_type"] = "pay_type"
    defaults["description"] = "description"
    defaults["cheque_count"] = "cheque_count"
    defaults.update(**kwargs)
    return Installment.objects.create(**defaults)


def create_installmentcheque(**kwargs):
    defaults = {}
    defaults["cheque_number"] = "cheque_number"
    defaults["bank_name"] = "bank_name"
    defaults["track_card_payment_number"] = "track_card_payment_number"
    defaults["description"] = "description"
    defaults["state"] = "state"
    defaults["due_date"] = "due_date"
    defaults["amount"] = "amount"
    defaults.update(**kwargs)
    if "installment" not in defaults:
        defaults["installment"] = create_installment()
    return InstallmentCheque.objects.create(**defaults)


class CompanyViewTest(unittest.TestCase):
    '''
    Tests for Company
    '''
    def setUp(self):
        self.client = Client()

    def test_list_company(self):
        url = reverse('transportation_company_company_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_company(self):
        url = reverse('transportation_company_company_create')
        data = {
            "manager_full_name": "manager_full_name",
            "manager_national_code": "manager_national_code",
            "name": "name",
            "avatar": "avatar",
            "email": "email",
            "website": "website",
            "active": "active",
            "phone_numbers": "phone_numbers",
            "capacity": "capacity",
            "service_types": "service_types",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_company(self):
        company = create_company()
        url = reverse('transportation_company_company_detail', args=[company.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_company(self):
        company = create_company()
        data = {
            "manager_full_name": "manager_full_name",
            "manager_national_code": "manager_national_code",
            "name": "name",
            "avatar": "avatar",
            "email": "email",
            "website": "website",
            "active": "active",
            "phone_numbers": "phone_numbers",
            "capacity": "capacity",
            "service_types": "service_types",
        }
        url = reverse('transportation_company_company_update', args=[company.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ContractViewTest(unittest.TestCase):
    '''
    Tests for Contract
    '''
    def setUp(self):
        self.client = Client()

    def test_list_contract(self):
        url = reverse('transportation_company_contract_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_contract(self):
        url = reverse('transportation_company_contract_create')
        data = {
            "status": "status",
            "service_type": "service_type",
            "commission_rate_contract": "commission_rate_contract",
            "source_loc": "source_loc",
            "destination_loc": "destination_loc",
            "source_address": "source_address",
            "destination_address": "destination_address",
            "side_way": "side_way",
            "special": "special",
            "installment": create_installment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_contract(self):
        contract = create_contract()
        url = reverse('transportation_company_contract_detail', args=[contract.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_contract(self):
        contract = create_contract()
        data = {
            "status": "status",
            "service_type": "service_type",
            "commission_rate_contract": "commission_rate_contract",
            "source_loc": "source_loc",
            "destination_loc": "destination_loc",
            "source_address": "source_address",
            "destination_address": "destination_address",
            "side_way": "side_way",
            "special": "special",
            "installment": create_installment().pk,
        }
        url = reverse('transportation_company_contract_update', args=[contract.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class AddressViewTest(unittest.TestCase):
    '''
    Tests for Address
    '''
    def setUp(self):
        self.client = Client()

    def test_list_address(self):
        url = reverse('transportation_company_address_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_address(self):
        url = reverse('transportation_company_address_create')
        data = {
            "name": "name",
            "point": "point",
            "address": "address",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_address(self):
        address = create_address()
        url = reverse('transportation_company_address_detail', args=[address.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_address(self):
        address = create_address()
        data = {
            "name": "name",
            "point": "point",
            "address": "address",
        }
        url = reverse('transportation_company_address_update', args=[address.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InstallmentViewTest(unittest.TestCase):
    '''
    Tests for Installment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_installment(self):
        url = reverse('transportation_company_installment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_installment(self):
        url = reverse('transportation_company_installment_create')
        data = {
            "name": "name",
            "amount": "amount",
            "status": "status",
            "pay_type": "pay_type",
            "description": "description",
            "cheque_count": "cheque_count",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_installment(self):
        installment = create_installment()
        url = reverse('transportation_company_installment_detail', args=[installment.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_installment(self):
        installment = create_installment()
        data = {
            "name": "name",
            "amount": "amount",
            "status": "status",
            "pay_type": "pay_type",
            "description": "description",
            "cheque_count": "cheque_count",
        }
        url = reverse('transportation_company_installment_update', args=[installment.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InstallmentChequeViewTest(unittest.TestCase):
    '''
    Tests for InstallmentCheque
    '''
    def setUp(self):
        self.client = Client()

    def test_list_installmentcheque(self):
        url = reverse('transportation_company_installmentcheque_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_installmentcheque(self):
        url = reverse('transportation_company_installmentcheque_create')
        data = {
            "cheque_number": "cheque_number",
            "bank_name": "bank_name",
            "track_card_payment_number": "track_card_payment_number",
            "description": "description",
            "state": "state",
            "due_date": "due_date",
            "amount": "amount",
            "installment": create_installment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_installmentcheque(self):
        installmentcheque = create_installmentcheque()
        url = reverse('transportation_company_installmentcheque_detail', args=[installmentcheque.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_installmentcheque(self):
        installmentcheque = create_installmentcheque()
        data = {
            "cheque_number": "cheque_number",
            "bank_name": "bank_name",
            "track_card_payment_number": "track_card_payment_number",
            "description": "description",
            "state": "state",
            "due_date": "due_date",
            "amount": "amount",
            "installment": create_installment().pk,
        }
        url = reverse('transportation_company_installmentcheque_update', args=[installmentcheque.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


