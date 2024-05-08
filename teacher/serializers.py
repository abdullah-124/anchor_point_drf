from rest_framework import serializers
from .models import Teacher
from django.contrib.auth.models import User

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Teacher
        fields = '__all__'
class UserSerialzer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = '__all__'