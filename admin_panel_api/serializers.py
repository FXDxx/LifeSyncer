from rest_framework import serializers
from .models import *

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'

class DoctorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['cnic', 'name']
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class PatientMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ['cnic', 'name']

