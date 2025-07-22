from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    return Response({
        "Diplay Home": "Homepage",
        "Dashboard": {
            
        }

    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_user(request):
    logout(request)
    messages.success(request,("User logged out"))
    return redirect('authentication/login.html')
