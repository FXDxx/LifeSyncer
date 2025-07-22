from django.contrib import admin
from .models import *
# Register your models here.
admin.register(DoctorLogin)
admin.register(PatientInfo)
admin.register(PatientMedication)
admin.register(PatientAppointments)
admin.register(PatientVitals)
admin.register(PatientLabReports)




