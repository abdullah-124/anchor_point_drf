from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserSerialzer, RegistrationSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
class Userview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer


class RegestrationApi_view(APIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            # login(user)
            return JsonResponse({'message':'Account created, please login'})
        return Response(serializer.errors)
    


class LoginApiView(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        print(self.request.data)
        if(serializer.is_valid()):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username,password)
            user = authenticate(username = username,password=password)
            if user :
                login(self.request,user)
                return JsonResponse({'message': 'Login successful',"user":user.id})
            else :
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        else:
            return JsonResponse({'message': 'Methods not allowed'}, status=405)
    
{
"username":"mdsakib",
"password":"lino1234"
}