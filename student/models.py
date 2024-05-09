from django.db import models
from django.contrib.auth.models import User
# from course.models import Course

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11,null=True)
    description = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='students/images',null=True)
    address = models.CharField(max_length=40,null=True)
    # enroll_courses = models.ManyToManyField(Course)
    def __str__(self) -> str:
        return self.user.username
    