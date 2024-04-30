from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer,UserSerialzer
from django.contrib.auth.models import User

# Create your views here.
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

