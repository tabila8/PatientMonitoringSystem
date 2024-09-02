from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse

# Create your models here.
class HospitalPersonnel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=14,unique=True,blank=True)

    def __str__(self):
        return self.user.username

#create Doctors models
class doctor_registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #patient = models.ManyToManyField(patient_registration)
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    Doctor_Name = models.CharField(max_length=100,blank=True)
    Designation = models.CharField(max_length=100,blank=True)
    stvalue = (
        ("Cardiology","Cardiology"),
        ("Neurology","Neurology"),
        ("Orthopaedics","Orthopaedics"),
        ("Gynecology","Gynecology")
    )
    Department = models.CharField(max_length=50,choices=stvalue,blank=True,null=True)
    Hospital_Name = models.CharField(max_length=250,blank=True)
    bvalue=(
        ("O-","O-"),
        ("O+","O+"),
        ("A-","A-"),
        ("A+","A+"),
        ("B-","B-"),
        ("B+","B+"),
        ("AB-","AB-"),
        ("AB+","AB+")
    )
    Blood_Group = models.CharField(max_length=5,choices=bvalue)
    Phone_No = models.CharField(max_length=14,unique=True,blank=True)

    def __str__(self):
        return self.Doctor_Name

    #to send primary primary key
    def get_absolute_url(self):
        #print(self.pk)
        return reverse('patientMonitor:doctor_details',kwargs={'pk':self.pk})


#create patient models
class patient_registration(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    Patient_Name = models.CharField(max_length=100,blank=True)
    Age = models.IntegerField(blank=True)
    svalue=(
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )
    sex = models.CharField(max_length=10,choices=svalue)
    bvalue=(
        ("O-","O-"),
        ("O+","O+"),
        ("A-","A-"),
        ("A+","A+"),
        ("B-","B-"),
        ("B+","B+"),
        ("AB-","AB-"),
        ("AB+","AB+")
    )
    Blood_Group = models.CharField(max_length=5,choices=bvalue)
    Weight = models.FloatField(blank=True)
    Height = models.IntegerField(blank=True)
    Ward_No = models.IntegerField(blank=True,null=True)
    Room_No = models.IntegerField(blank=True,null=True)
    Bed_No = models.IntegerField(blank=True,null=True)
    Phone_No = models.CharField(max_length=14,blank=True)
    slug = models.SlugField(max_length=1264,unique=True)
    stvalue = (
        ("Cardiology","Cardiology"),
        ("Neurology","Neurology"),
        ("Orthopaedics","Orthopaedics"),
        ("Gynecology","Gynecology")
    )
    Department = models.CharField(max_length=50,choices=stvalue,blank=True,null=True)
    mvalue = (
        ("Hospital","Hospital"),
        ("Home","Home")
    )
    Monitoring = models.CharField(max_length=50,choices=mvalue,blank=True,null=True)
    #doctor = models.ManyToManyField(doctor_registration)
    doctor = models.ForeignKey(doctor_registration,on_delete=models.CASCADE, null=True, related_name='patient_list')
    # demo = models.ForeignKey(Demo,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.Patient_Name

    def get_absolute_url(self):
        #print(self.pk)
        return reverse('patientMonitor:patient_details',kwargs={'pk':self.pk})

#Temperature Sensor
class sensors(models.Model):
    Temperature = models.FloatField(blank=True,null=True)
    Pulse_Rate = models.IntegerField(blank=True,null=True)
    Oxygen_Saturation = models.IntegerField(blank=True,null=True)
    scall = (
        ("Yes","Yes"),
        ("No","No")
    )
    call = models.CharField(max_length=5,choices=scall, null=True,blank=True)
    Patient = models.ForeignKey(patient_registration,on_delete= models.CASCADE,related_name='sensors_list',null=True)

    
    def get_absolute_url(self):
        return reverse('patientMonitor:patient_information')




#Prescription Section
class prescription(models.Model):
    patient = models.ForeignKey(patient_registration,on_delete=models.CASCADE,related_name='patient_prescription')
    Doctor = models.ForeignKey(doctor_registration, on_delete=models.CASCADE,related_name='doctor_prescription',null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    prescription = models.TextField()
    prescription_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-prescription_date',]

    def __str__(self):
        return self.prescription

    def get_absolute_url(self):
        #print(self.pk)
        return reverse('patientMonitor:patient_information')


#Ambulance Section
class ambulance(models.Model):
    Driver_Name = models.CharField(max_length=200,blank=True)
    Contact_No = models.CharField(max_length=14,blank=True)
    Ambulance_No = models.CharField(max_length=14,blank=True,unique=True)
    Hospital_Name = models.CharField(max_length=200,blank=True)
    Availability = models.BooleanField()

    def __str__(self):
        return self.Ambulance_No

    def get_absolute_url(self):
            #print(self.pk)
        return reverse('patientMonitor:index')
