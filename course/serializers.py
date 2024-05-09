from rest_framework import serializers
from .models import Course,Enroll,Reviews,Category

class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    class Meta:
        model = Course
        fields = '__all__'

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = '__all__'

class CheckoutSerializer(serializers.Serializer):
    course_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    mobile_number = serializers.CharField(max_length=12,required=True)

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'