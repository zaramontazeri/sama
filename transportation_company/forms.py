from django import forms
from .models import Company, Contract, Address, Installment, InstallmentCheque


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['manager_full_name', 'manager_national_code', 'avatar', 'email', 'website', 'active', 'phone_numbers', 'capacity', 'service_types']


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['status', 'service_type', 'commission_rate_contract', 'source_loc', 'destination_loc', 'source_address', 'destination_address', 'side_way', 'special', 'installment']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'point', 'address']


class InstallmentForm(forms.ModelForm):
    class Meta:
        model = Installment
        fields = ['amount', 'status', 'pay_type', 'description', 'cheque_count']


class InstallmentChequeForm(forms.ModelForm):
    class Meta:
        model = InstallmentCheque
        fields = ['cheque_number', 'bank_name', 'track_card_payment_number', 'description', 'state', 'due_date', 'amount', 'installment']


