from django.contrib import admin
from patientMonitor.models import HospitalPersonnel, patient_registration,doctor_registration,sensors,prescription,ambulance

# Register your models here.
admin.site.register(HospitalPersonnel)
admin.site.register(patient_registration)
admin.site.register(doctor_registration)
admin.site.register(sensors)
admin.site.register(prescription)
admin.site.register(ambulance)
