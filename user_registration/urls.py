from django.urls import path
from . import views

urlpatterns=[
    path('api/login_user/', views.login_user),
    path('api/homepage/', views.display_home),
    path('api/user_logout/', views.login_user),
]