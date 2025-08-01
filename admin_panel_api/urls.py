from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('api/dashboard', views.show_dashboard_list),
    path('api/dashboard/doctors',views.show_doctors_list),
    path('api/dashboard/patient',views.show_patients_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)