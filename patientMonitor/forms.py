from django import forms
from django.contrib.auth.models import User
from patientMonitor.models import HospitalPersonnel,patient_registration,doctor_registration

import random

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')
        #fields = '__all__'

class HospitalPersonnelForm(forms.ModelForm):
    class Meta():
        model = HospitalPersonnel
        fields = ('phone_no',)

#patient Registration forms

class patient_registrationForm(forms.ModelForm):
    Patient_Name = forms.CharField(required=True)
    slug = forms.SlugField(label='Patient ID')
    class Meta():
        model = patient_registration
        #fields = ('Patient_Name','Age','sex','Blood_Group','Weight','Height','Ward_No','Room_No','Bed_No','Phone_No','doctor')
        fields = '__all__'

#doctor Registration forms
class doctor_registrationForm(forms.ModelForm):
    Doctor_Name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=20,required=True)
    class Meta():
        model = doctor_registration
        fields = ('Doctor_Name','Designation','Department','Hospital_Name','Blood_Group','Phone_No')
