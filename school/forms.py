from django import forms
from .models import Parent, Student, School

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['full_name', 'emergency_numbers', 'national_code', 'gender', 'address_point', 'address', 'user']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'national_code', 'gender', 'student_code', 'parent', 'user', 'school']


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'manager_full_name', 'phone_numbers', 'time_shifts', 'manager_mobile', 'manager_national_number', 'working_time', 'address', 'address_point', 'deputy_mobile', 'deputy_full_name', 'service_officer', 'avatar', 'postal_code', 'student_count']
