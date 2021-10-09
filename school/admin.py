from django.contrib import admin
from django import forms
from .models import City, Level, Parent, Region, Student, School

class ParentAdminForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = '__all__'


class ParentAdmin(admin.ModelAdmin):
    form = ParentAdminForm
    list_display = ['created', 'last_updated', 'full_name', 'emergency_numbers', 'national_code', 'gender', 'address_point', 'address']
    readonly_fields = []

admin.site.register(Parent, ParentAdmin)


class StudentAdminForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = ['created', 'last_updated', 'full_name', 'national_code', 'gender', 'student_code']
    readonly_fields = []

admin.site.register(Student, StudentAdmin)


class SchoolAdminForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'

class RegionAdmin(admin.ModelAdmin):
    form = SchoolAdminForm
    list_display = ['name']
    readonly_fields = []

admin.site.register(Region, RegionAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = []

admin.site.register(City, CityAdmin)

class SchoolAdmin(admin.ModelAdmin):
    form = SchoolAdminForm
    list_display = ['name', 'created', 'last_updated', 'manager_full_name', 'phone_numbers', 'manager_mobile', 'manager_national_number', 'address', 'address_point', 'deputy_mobile', 'deputy_full_name', 'service_officer', 'avatar', 'postal_code', 'student_count']
    readonly_fields = []

admin.site.register(School, SchoolAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ["level","part"]
    readonly_fields = []

admin.site.register(Level, LevelAdmin)