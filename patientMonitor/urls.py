from django.contrib import admin
from django.urls import path
from patientMonitor import views
from django.conf.urls import url
from django.conf import settings
from patientMonitor import views

app_name = "patientMonitor"

urlpatterns = [
    path('',views.index, name='index'),
    #path('patient_info/',views.patient_details1.as_view(),name='patient_info'),
    path('patient_registration/',views.patient_registration, name='patient_registration'),
    path('doctor_registration/',views.doctor_registration, name='doctor_registration'),
    #path('patient_information/',views.patient_information, name='patient_information'),
    path('hospitalPersonnelRegister/',views.hospitalPersonnelRegister,name='hospitalPersonnelRegister'),
    path('admin_login_page/',views.admin_login_page,name='admin_login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('patient_information/',views.patient_information.as_view(),name='patient_information'),
    path('doctor_list/',views.doctor_list.as_view(),name='doctor_list'),
    path('doctor_details/<pk>/',views.doctor_details.as_view(),name='doctor_details'),
    path('patient_details/<pk>',views.patient_details.as_view(),name='patient_details'),
    path('patient_data_input/',views.patient_data_input.as_view(),name='patient_data_input'),
    path('prescription/<pk>/',views.patient_prescription.as_view(),name='prescription'),
    path('add_prescription/',views.addPrescription.as_view(),name='add_prescription'),
    path('cardiology/',views.cardiology.as_view(),name='cardiology'),
    path('neurology/',views.neurology.as_view(),name='neurology'),
    path('orthopaedics/',views.orthopaedics.as_view(),name='orthopaedics'),
    path('gynecology/',views.gynecology.as_view(),name='gynecology'),
    path('n_cardiology/',views.n_cardiology.as_view(),name='n_cardiology'),
    path('n_neurology/',views.n_neurology.as_view(),name='n_neurology'),
    path('n_orthopaedics/',views.n_orthopaedics.as_view(),name='n_orthopaedics'),
    path('n_gynecology/',views.n_gynecology.as_view(),name='n_gynecology'),
    path('registration_form/',views.registration_form.as_view(),name='registration_form'),
    path('d_cardiology/',views.d_cardiology.as_view(),name='d_cardiology'),
    path('d_neurology/',views.d_neurology.as_view(),name='d_neurology'),
    path('d_orthopaedics/',views.d_orthopaedics.as_view(),name='d_orthopaedics'),
    path('d_gynecology/',views.d_gynecology.as_view(),name='d_gynecology'),
    path('p_cardiology/',views.p_cardiology.as_view(),name='p_cardiology'),
    path('p_neurology/',views.p_neurology.as_view(),name='p_neurology'),
    path('p_orthopaedics/',views.p_orthopaedics.as_view(),name='p_orthopaedics'),
    path('p_gynecology/',views.p_gynecology.as_view(),name='p_gynecology'),
    path('home_monitor/',views.homeMonitor.as_view(),name='home_monitor'),
    path('emergencyAlert/',views.emergencyAlert.as_view(),name='emergencyAlert'),
    path('add_ambulance/',views.addAmbulance.as_view(),name='add_ambulance'),
    path('ambulance_list/',views.ambulance_list.as_view(),name='ambulance_list'),
    path('ambulance_details/<pk>/',views.ambulance_details.as_view(),name='ambulance_details'),
    path('ambulance_booked/<pk>/',views.ambulance_booked.as_view(),name='ambulance_booked'),
    path('mailsend/',views.mailsend,name='mailsend'),
]
