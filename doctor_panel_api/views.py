from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import FileResponse, Http404
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def signup_doctor(request):
    username = request.data.get("username")
    password = request.data.get("password")

    DoctorLogin.objects.create(
        username=username,
        password=password,
    )
    return Response({
            "message":"Login successfully"}, status=status.HTTP_200_OK)
  
    

@api_view(['GET'])
def display_home(request):
    try:
        patient_info_data = PatientInfo.objects.all()
        patient_medication_data=PatientMedication.objects.all()
        patient_appointments_data=PatientAppointments.objects.all()
        patient_vitals_data=PatientVitals.objects.all()
        patient_lab_data=PatientLabReports.objects.all()

        info_serializer = PatientInfoSerializer(patient_info_data, many= True)
        medication_serializer=PatientMedicationSerializer(patient_medication_data, many=True)
        appointments_serializer=PatientAppointmentsSerializer(patient_appointments_data, many=True)
        vitals_serializers=PatientVitalsSerializer(patient_vitals_data, many=True)
        lab_serializers=PatientLabReportsSerializer(patient_lab_data, many=True)

        return Response({
                        "patient":info_serializer.data,
                         "medications": medication_serializer.data,
                         "appointments":appointments_serializer.data,
                         "vitals":vitals_serializers.data,
                         "lab_serializers":lab_serializers.data,
                         }, status=status.HTTP_200_OK)
    except PatientInfo.DoesNotExist:
        return Response({"Error:": "invalid url or user not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST','GET','PUT', 'PATCH', 'DELETE'])
def update_patient_data(request, cnic):
    
    if request.method == 'POST':
        if PatientContactInfo.objects.filter(patient__cnic=cnic).exists():
            return Response({"message":"patient already exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        cnic=cnic
        patient_name=request.data.get("patient_name")
        patient_age=request.data.get("patient_age")
        patient_gender= request.data.get("patient_gender")
        patient_photo=request.data.get("patient_photo")
        patient_status=request.data.get("patient_status")
        patient_diagnosis= request.data.get("patient_diagnosis")
        patient_phone = request.data.get("patient_phone")
        patient_email = request.data.get("patient_email")
        
        patient_data = PatientInfo.objects.create(
            cnic=cnic,
            patient_name=patient_name,
            patient_age=patient_age,
            patient_gender=patient_gender,
            patient_photo=patient_photo,
            patient_status=patient_status,
            patient_diagnosis=patient_diagnosis,
        )
        print("p2")
        PatientContactInfo.objects.create(
            patient=patient_data,
            patient_phone=patient_phone,
            patient_email=patient_email,
        )
        print("p3")
        return Response({"message":"Patient data updated..contact data updated"}, status=status.HTTP_201_CREATED)
    
    try:
        patient_data = PatientInfo.objects.get(cnic=cnic)
        patient_contact_data = PatientContactInfo.objects.filter(patient=patient_data)
    except PatientInfo.DoesNotExist:
        return Response({"message":"patient does not exists"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        info_serializer = PatientInfoSerializer(patient_data, many=True)
        contact_serializer = PatientContactSerializer(patient_contact_data, many=True)
        return Response({"patient: ":info_serializer.data, "contact": contact_serializer.data}, status=status.HTTP_200_OK)    
    
    if request.method == 'PUT':
        #"cnic":cnic,
        patient_data.patient_name=request.data.get("patient_name")
        patient_data.patient_age=request.data.get("patient_age")
        patient_data.patient_gender= request.data.get("patient_gender")
        patient_data.patient_photo=request.data.get("patient_photo")
        patient_data.patient_status=request.data.get("patient_status")
        patient_data.patient_diagnosis= request.data.get("patient_diagnosis")
        #patient_data.save()
        
        if patient_contact_data:
            patient_contact_data.patient_phone= request.data.get("patient_phone"),
            patient_contact_data.patient_email= request.data.get("patient_email"),
            #patient_contact_data.save()
        return Response({"message":"patient data updated successfully"}, status=status.HTTP_202_ACCEPTED)
    
    if request.method == 'DELETE':
        if not patient_data:
            return Response({"message": "patient not found"}, status=status.HTTP_404_NOT_FOUND)
        patient_contact_data.delete()
        patient_data.delete()
        return Response({"message":"Patient data deleted successfully"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_lab_report(request, cnic):
    try:
        report = PatientLabReports.objects.filter(patient_id__cnic=cnic).first()
        if not report:
            return Response({"error": "No report found for this CNIC"}, status=status.HTTP_404_NOT_FOUND)
        
        return FileResponse(report.patient_report.open(), content_type='application/pdf')
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def display_dashboard(request):
    patient_data = PatientInfo.objects.all()
    patient_contact_data = PatientInfo.objects.all()
    patient_last_visit_date = PatientAppointments.objects.all()

    if not patient_data.exists() and not patient_contact_data.exists() and not patient_last_visit_date.exists():
        return Response({"error:", "data not found"}, status=status.HTTP_204_NO_CONTENT)
    
    patient_info_serializer = PatientInfoSerializer(patient_data, many=True)
    contact_serializer = PatientContactSerializer(patient_contact_data, many=True)
    patient_last_visit_serializer = PatientAppointmentsSerializer(patient_last_visit_date)
    

    
    
    return Response({
        "Patient data: ": patient_info_serializer.data,
        "Contact: ": contact_serializer.data,
        "Last visit: ": patient_last_visit_serializer.data
        }, status=status.HTTP_200_OK)


    


@api_view(['POST'])
def logout_user(request):
    logout(request)
    messages.success(request,("User logged out"))
    return redirect('authentication/login.html')
