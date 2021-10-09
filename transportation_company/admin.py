from django.contrib import admin
from django import forms
from .models import Company, Contract, Address, DriverContract, Installment, InstallmentCheque

class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = ['created', 'last_updated','name', 'manager_full_name', 'manager_national_code', 'avatar', 'email', 'website', 'active', 'phone_numbers', 'capacity', 'service_types']

admin.site.register(Company, CompanyAdmin)


class ContractAdminForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = '__all__'


class ContractAdmin(admin.ModelAdmin):
    form = ContractAdminForm
    list_display = ['created', 'last_updated', 'status', 'service_type', 'commission_rate_contract', 'source_loc', 'destination_loc', 'source_address', 'destination_address', 'side_way', 'special']

admin.site.register(Contract, ContractAdmin)


class DriverContractAdminForm(forms.ModelForm):

    class Meta:
        model = DriverContract
        fields = '__all__'


class DriverContractAdmin(admin.ModelAdmin):
    form = DriverContractAdminForm
    list_display = ['created', 'last_updated', 'start_date', 'end_date', 'salari', 'salari_type', 'price_increase']
    readonly_fields = ['created', 'last_updated']

admin.site.register(DriverContract, DriverContractAdmin)



class AddressAdminForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = '__all__'


class AddressAdmin(admin.ModelAdmin):
    form = AddressAdminForm
    list_display = ['name', 'created', 'last_updated', 'point', 'address']
    readonly_fields = [ 'created', 'last_updated']

admin.site.register(Address, AddressAdmin)


class InstallmentAdminForm(forms.ModelForm):

    class Meta:
        model = Installment
        fields = '__all__'


class InstallmentAdmin(admin.ModelAdmin):
    form = InstallmentAdminForm
    list_display = [  'created', 'last_updated', 'amount', 'status', 'pay_type', 'description', 'cheque_count']

admin.site.register(Installment, InstallmentAdmin)


class InstallmentChequeAdminForm(forms.ModelForm):

    class Meta:
        model = InstallmentCheque
        fields = '__all__'


class InstallmentChequeAdmin(admin.ModelAdmin):
    form = InstallmentChequeAdminForm
    list_display = ['cheque_number', 'created', 'last_updated', 'bank_name', 'track_card_payment_number', 'description', 'state', 'due_date', 'amount']

admin.site.register(InstallmentCheque, InstallmentChequeAdmin)


