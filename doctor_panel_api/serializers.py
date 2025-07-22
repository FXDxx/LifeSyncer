from rest_framework import serializers
from .models import *

class DoctorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorLogin
        fields = ['username']

class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'

class PatientMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientMedication
        fields = '__all__'

class PatientAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientAppointments
        fields = '__all__'

class PatientVitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientVitals
        fields = '__all__'

class PatientLabReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientLabReports
        fields = '__all__'

class PatientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientContactInfo
        fields = '__all__'
        
