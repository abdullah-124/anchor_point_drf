from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User 
from .serializers import UserSerialzer
# Create your views here.
class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

