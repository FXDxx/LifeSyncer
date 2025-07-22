from django.db import models

# Create your models here.
class DoctorLogin(models.Model):
    username = models.CharField(max_length=100, null=False)
    password= models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
    

class PatientInfo(models.Model):
    cnic = models.CharField(max_length=15, null=False, primary_key=True)
    patient_name= models.CharField(max_length=100, null=False)
    patient_age = models.IntegerField(null=True)
    patient_gender=models.CharField(max_length=11, null=False)
    patient_photo=models.ImageField(upload_to="media", null=True, blank=True)
    patient_status=models.CharField(max_length=20, null=True)
    patient_diagnosis=models.TextField(max_length=200,null=True)
    def __str__(self):
        return self.cnic, self.patient_name, self.patient_age, self.patient_gender, self.patient_status, self.patient_diagnosis
    
class PatientMedication(models.Model):
    patient_id=models.ForeignKey(PatientInfo, to_field='cnic', on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100, null=True)
    medication_dosage=models.IntegerField(null=False)
    medication_frequency= models.IntegerField(null=True)
    medication_timing=models.CharField(max_length=50, null=True)
    medication_start_time= models.DateField()
    medication_end_time= models.DateField()

    def __str__(self):
        return self.medication_name

class PatientAppointments(models.Model):
    patient_id=models.ForeignKey(PatientInfo,to_field='cnic', on_delete=models.CASCADE)
    recent_visit_date=models.DateField()
    next_visit_date=models.DateField()

    def __str__(self):
        return self.recent_visit_date

class PatientVitals(models.Model):
    patient_id=models.ForeignKey(PatientInfo,to_field='cnic', on_delete=models.CASCADE)
    patient_tempreture=models.IntegerField(null=True)
    patient_blood_pressure=models.IntegerField(null=True)
    patient_glucose_level=models.IntegerField(null=True)
    patient_weight= models.IntegerField(null=True)
    patient_stress=models.CharField(max_length=20)
    patient_oxygen= models.CharField(max_length=30)

    def __str__(self):
        return self.patient_id

class PatientLabReports(models.Model):
    patient_id=models.ForeignKey(PatientInfo,to_field='cnic', on_delete=models.CASCADE)
    patient_report = models.FileField(upload_to='documents')
    def __str__(self):
        return self.patient_id
    
class PatientContactInfo(models.Model):
    patient=models.ForeignKey(PatientInfo,to_field='cnic', on_delete=models.CASCADE)
    patient_phone=models.IntegerField(null=True)
    patient_email=models.CharField(max_length=100, null=True)