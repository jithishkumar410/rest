
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import login, authenticate, logout
from .serialzers import Demos,Learn
from .validate import custom_validation
from rest_framework.authtoken.models import Token
from .models import Demo
from rest_framework import permissions, status

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

@api_view(['POST'])

def addusr(request):
    print(request.data)
    clean_data = custom_validation(request.data)
    s=Learn(data=clean_data)
    if s.is_valid(raise_exception=True):
	    user = s.create(clean_data)
	    if user:
              return Response(s.data,status=200)
    return Response(status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login(request):
    username = request.data.get('email')
    password = request.data.get('password')
    print(username,password)
    u=User.objects.filter(email=username,password=password)
    print(u)
    user = authenticate(request,email=username, password=password)
    
   
    if user:
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

     
