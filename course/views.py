from django.shortcuts import render
from rest_framework import viewsets
from .models import Course,Reviews,Category,Enroll
from .serializers import CourseSerializer,ReviewsSerializer,CategorySerializer,EnrollSerializer

# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
class EnrollView(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer

class ReviewsView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

