from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Course,Reviews,Category,Enroll
from .serializers import CourseSerializer,ReviewsSerializer,CategorySerializer,EnrollSerializer,CheckoutSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from student.models import Student


# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
class EnrollView(viewsets.ModelViewSet):
    queryset = Enroll.objects.all()
    serializer_class = EnrollSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id')
        if student_id:
            queryset = queryset.filter(student = student_id)
        return queryset

class ReviewsView(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CheckoutApiView(APIView):
    serializer_class = CheckoutSerializer
    def post(self,request):
        serializer = CheckoutSerializer(data=request.data)
        # print(self.request.data)
        if(serializer.is_valid()):
            course_id = serializer.validated_data['course_id']
            user_id = serializer.validated_data['user_id']
            mobile_number = serializer.validated_data['mobile_number']
            user = User.objects.get(id=user_id)
            student = Student.objects.get(user = user)
            student.save()
            course = Course.objects.get(id=course_id)
            enroll_course = Enroll.objects.create(student=student,course=course,mobile_number=mobile_number)
            enroll_course.save()
            return JsonResponse({'message': 'Enrolled successfull',"student_id":student.id}, status=200)
        return JsonResponse({'message': 'invalid data'}, status=401)
            
        

