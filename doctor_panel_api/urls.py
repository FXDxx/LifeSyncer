from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('api/homepage/', views.display_home, name="display_home"),
    path('api/homepage/view-report/<str:cnic>', views.view_lab_report, name="view_report"),
    path('api/homepage/update-data/<str:cnic>', views.update_patient_data, name="update-patient"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)