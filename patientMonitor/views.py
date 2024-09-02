from django.shortcuts import render
from django.http import HttpResponse
from patientMonitor.forms import UserForm, HospitalPersonnelForm, patient_registrationForm, doctor_registrationForm
from patientMonitor.models import HospitalPersonnel
from django.contrib.auth.models import User
from patientMonitor import models

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.db import IntegrityError
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView,CreateView


# Create your views here.
def index(request):
    diction = {'title':'Home Page'}
    return render(request, 'patientMonitor/index.html', context=diction)

#def patient_information(request):
    #diction = {'title': 'Patient Information'}
    #return render(request,'patientMonitor/patient_information.html', context=diction)

#hospital admin registration
def hospitalPersonnelRegister(request):
    registered = False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        hospital_personnel_form = HospitalPersonnelForm(data=request.POST)
        if user_form.is_valid() and hospital_personnel_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            hospitalPersonnel=hospital_personnel_form.save(commit=False)
            hospitalPersonnel.user=user
            hospitalPersonnel.save()
            registered=True
    else:
        user_form = UserForm()
        hospital_personnel_form = HospitalPersonnelForm()

    diction = {'title':'Hospital Personnel Registration','user_form':user_form,'hospital_personnel_form':hospital_personnel_form,'registered':registered}
    return render(request,'patientMonitor/hospitalPersonnelRegister.html',context=diction)

#admin login view
def admin_login_page(request):
    diction={}
    return render(request,'patientMonitor/admin_login.html',context=diction)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                print("Login Successfull!!")
                return HttpResponseRedirect(reverse('patientMonitor:index'))
            else:
                print("Inactive user")
                return HttpResponseRedirect(reverse('patientMonitor:hospitalPersonnelRegister'))
        else:
            print("Wrong user")
            return HttpResponseRedirect(reverse('patientMonitor:admin_login_page'))
    else:
        print("not post")
        return HttpResponseRedirect(reverse('patientMonitor:index'))
#logout admin
@login_required
def admin_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('patientMonitor:index'))

#patient registration forms
def patient_registration(request):
    registered = False
    if request.method=='POST':
        #user_form = UserForm(data=request.POST)
        patient_registration_form = patient_registrationForm(data=request.POST)
        if patient_registration_form.is_valid():
            #user = user_form.save()
            #user.set_password(user.password)
            #user.save()
            patient_register=patient_registration_form.save(commit=False)
            #patient_register.user=user
            patient_register.save()
            registered=True
    else:
        #user_form = UserForm()
        patient_registration_form = patient_registrationForm()

    diction = {'title': 'Patient Registration Form','patient_registration_form':patient_registration_form,'registered':registered}
    return render(request,'patientMonitor/patient_registration.html', context=diction)

#doctor registration forms
def doctor_registration(request):
    registered = False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        doctor_registration_form = doctor_registrationForm(data=request.POST)
        if user_form.is_valid() and doctor_registration_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            doctor_register=doctor_registration_form.save(commit=False)
            doctor_register.user=user
            doctor_register.save()
            registered=True
    else:
        user_form = UserForm()
        doctor_registration_form = doctor_registrationForm()


    diction = {'title': 'Doctor Registration Form','doctor_registration_form':doctor_registration_form,'user_form=':user_form,'registered':registered}
    return render(request,'patientMonitor/doctor_registration.html', context=diction)


#here I create calssbased view
#def patient_information(request):
    #diction = {'title': 'Patient Information'}
    #return render(request,'patientMonitor/patient_information.html', context=diction)
#patients list
class patient_information(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/patient_information.html'

#doctors list
class doctor_list(ListView):
    context_object_name = 'doctor_list'
    model = models.doctor_registration
    template_name = 'patientMonitor/doctor_list.html'

#doctors Details
class doctor_details(DetailView):
    context_object_name = 'doctor_registration'
    model = models.doctor_registration
    template_name = 'patientMonitor/doctor_details.html'

#patients details
class patient_details(DetailView):
    context_object_name = 'patient_registration'
    model = models.patient_registration
    template_name = 'patientMonitor/patient_details.html'

#patient Data input
class patient_data_input(TemplateView):
    template_name = 'patientMonitor/patient_data_input.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context





#prescription section
#@login_required
class patient_prescription(DetailView):
    context_object_name = 'patient_registration'
    model = models.patient_registration
    template_name = 'patientMonitor/prescription.html'

class addPrescription(CreateView):
    fields = ('patient','Doctor','prescription')
    model = models.prescription
    template_name = 'patientMonitor/add_prescription.html'




#patient monitor
class cardiology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/cardiology.html'

class neurology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/neurology.html'

class orthopaedics(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/orthopaedics.html'

class gynecology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/gynecology.html'

class n_cardiology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/n_cardiology.html'

class n_neurology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/n_neurology.html'

class n_orthopaedics(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/n_orthopaedics.html'

class n_gynecology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/n_gynecology.html'

#registration of patient and doctor_register
class registration_form(TemplateView):
    template_name = 'patientMonitor/registration.html'


#doctors list Department wise
class d_cardiology(ListView):
    context_object_name = 'doctor_list'
    model = models.doctor_registration
    template_name = 'patientMonitor/d_cardiology.html'

class d_neurology(ListView):
    context_object_name = 'doctor_list'
    model = models.doctor_registration
    template_name = 'patientMonitor/d_neurology.html'

class d_orthopaedics(ListView):
    context_object_name = 'doctor_list'
    model = models.doctor_registration
    template_name = 'patientMonitor/d_orthopaedics.html'

class d_gynecology(ListView):
    context_object_name = 'doctor_list'
    model = models.doctor_registration
    template_name = 'patientMonitor/d_gynecology.html'

#patient list Department wise
class p_cardiology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/p_cardiology.html'

class p_neurology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/p_neurology.html'

class p_orthopaedics(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/p_orthopaedics.html'

class p_gynecology(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/p_gynecology.html'


#home Monitoring
class homeMonitor(ListView):
    context_object_name = 'patient_list'
    model = models.patient_registration
    template_name = 'patientMonitor/home_monitor.html'

#emergency Alert
class emergencyAlert(ListView):
    context_object_name = 'patient_registration'
    model = models.patient_registration
    template_name = 'patientMonitor/emergencyAlert.html'

#ambulance formation
class addAmbulance(CreateView):
    fields = '__all__'
    model = models.ambulance
    template_name = 'patientMonitor/add_ambulance.html'

class ambulance_list(ListView):
    context_object_name = 'ambulance_list'
    model = models.ambulance
    template_name = 'patientMonitor/ambulance_list.html'

class ambulance_details(DetailView):
    context_object_name = 'ambulance'
    model = models.ambulance
    template_name = 'patientMonitor/ambulance_details.html'

class ambulance_booked(UpdateView):
    fields = ('Availability',)
    model = models.ambulance
    template_name = 'patientMonitor/add_ambulance.html'


#email send
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def mailsend(request):
    template = render_to_string('patientMonitor/patient_details.html',{})

    email = EmailMessage(
        'Emergency',
        template,
        'smartiotmonitoringsystem@gmail.com',
        ['mmamun161142@bscse.uiu.ac.bd',],
    )

    email.fail_silently = False
    email.send()

    return render(request,'patientMonitor/index.html',context={})
