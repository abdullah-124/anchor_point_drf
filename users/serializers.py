from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password',]
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        f = self.validated_data['first_name']
        l = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if(password != password2):
            raise serializers.ValidationError({'error':"Password dosen't match"})
        # if User.objects.filter(email = email).exists():
        #     raise serializers.ValidationError({'error':"Eamil already exists"})
        account = User(username = username, email=email,first_name = f,last_name = l)
        account.set_password(password)
        account.save()
        return account
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)