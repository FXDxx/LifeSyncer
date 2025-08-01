from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns=[
    path('api/signup', views.signup_doctor),
    path('api/homepage/', views.display_home, name="display_home"),
    path('api/homepage/view-report/<str:cnic>', views.view_lab_report, name="view_report"),
    path('api/homepage/update-data/<str:cnic>', views.update_patient_data, name="update-patient"),
    path('api/dashboard/', views.display_dashboard, name="dashboard"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)