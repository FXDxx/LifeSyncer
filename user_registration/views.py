from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from doctor_panel_api.models import *
from doctor_panel_api.serializers import *
# Create your views here.

@api_view(['POST'])
def login_user(request):
    print(request.data)
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    print("Authentication: ",user)
    if user is not None:
        return Response({
            "message":"Login successfully",
            "user":{
                "id":user.id,
                "username":username
            },
            "Home Page":{
                "Dashboard":"white background"
            },
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "message":"Page not found",
        }, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def display_home(request):
    patient_medication_data = PatientMedication.objects.all()
    patient_appointment_data = PatientAppointments.objects.all()
    patient_vitals_data = PatientVitals.objects.all()

    try:
        medication_serializer = PatientMedicationSerializer(patient_medication_data, many=True)
        appointment_serializer = PatientAppointmentsSerializer(patient_appointment_data, many=True)
        vitals_serializer = PatientVitalsSerializer(patient_vitals_data, many=True)

        return Response({"medication": medication_serializer.data,
                         "appointment": appointment_serializer.data,
                         "vitals":vitals_serializer.data},status=status.HTTP_200_OK)
    except PatientMedication.DoesNotExist:
        return Response({"message":"No data exists"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def update_vitals(request):
    #patient=request.data.get("patient")
    patient_tempreture= request.data.get("patient_tempreture")
    patient_blood_pressure= request.data.get("patient_blood_pressure")
    patient_glucose_level= request.data.get("patien_glucose_level")
    patient_weight=request.data.get("patient_weight")
    patient_stress=request.data.get("patient_stress")
    patient_oxygen=request.data.get("patient_oxygen")

    PatientVitals.objects.create(
        #patient=patient,
        patient_tempreture=patient_tempreture,
        patient_blood_pressure=patient_blood_pressure,
        patient_glucose_level=patient_glucose_level,
        patient_weight=patient_weight,
        patient_stress=patient_stress,
        patient_oxygen=patient_oxygen,
    )
    return Response({"message":"Vitals Data updated successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logout_user(request):
    logout(request)
    messages.success(request,("User logged out"))
    return redirect('authentication/login.html')
