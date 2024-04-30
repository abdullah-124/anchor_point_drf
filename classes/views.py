from django.shortcuts import render
from rest_framework import viewsets
from .models import Contents
from .serializers import ContentsSerializer

# Create your views here.
class ContentsView(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentsSerializer