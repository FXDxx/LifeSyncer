from django.db import models

# Create your models here.
class Doctors(models.Model):
    name=models.CharField(max_length=100, null=False)
    cnic=models.CharField(max_length=15, null=False, unique=True)
    phone=models.IntegerField()
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)

class Patients(models.Model):
    doctor = models.ForeignKey(Doctors, to_field='cnic', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    cnic=models.CharField(max_length=100, unique=True)
    phone=models.IntegerField()
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)



