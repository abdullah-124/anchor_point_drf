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
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
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
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("token",token,"/: uid",uid)
            confirm_link = f"https://anchor-point-drf.onrender.com/users/active/{uid}/{token}"
            email_sub = 'Email Confirmation'
            email_body = render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email = EmailMultiAlternatives(email_sub,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
        return JsonResponse({"message":"Check you mail to confirmation"})
    


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
                # token,create = Token.objects.get_or_create(user = user)
                return JsonResponse({'message': 'Login successful',"user":user.id})
            else :
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        else:
            return JsonResponse({'message': 'Methods not allowed'}, status=405)
        


def activate(self,uid64,token):
    try: 
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('register')
    else :
        return redirect('register')
    
    
{
"username":"mdsakib",
"password":"lino1234"
}