from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def show_doctors_list(request):
    doctor_data = Doctors.objects.all()
    try:
        doctor_serializer = DoctorSerializer(doctor_data, many=True)
        return Response({"User: Doctor": doctor_serializer.data}, status=status.HTTP_200_OK)
    except Doctors.DoesNotExist:
        return Response({"message":"No doctor found"}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['GET'])
def show_patients_list(request):
    patient_data=Patients.objects.all()
    try:
        patient_serializer= PatientSerializer(patient_data, many=True)
        return Response({"User: Patient": patient_serializer.data}, status=status.HTTP_200_OK)
    except Patients.DoesNotExist:
        return Response({"message":"No doctor found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def show_dashboard_list(request):
    user_doctor_data = Doctors.objects.all()
    user_patient_data = Patients.objects.all()
    try:
        user1_serializer= DoctorMiniSerializer(user_doctor_data, many=True)
        user2_serializer= PatientMiniSerializer(user_patient_data, many=True)

        return Response({"Doctor Data: ": user1_serializer.data,
                         "Patient Data: ": user2_serializer.data}, status=status.HTTP_200_OK)
    except Doctors.DoesNotExist:
        return Response({"message":"No doctor found"}, status=status.HTTP_204_NO_CONTENT)
    except Patients.DoesNotExist:
        return Response({"message":"No patient found"}, status=status.HTTP_204_NO_CONTENT)

    