from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from .models import Demo
from django.core.exceptions import ValidationError
class Demos(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'

class Learn(serializers.ModelSerializer):
    class Meta(object):
        model=User
        fields = ['username','email', 'password']

