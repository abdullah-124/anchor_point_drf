from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    description = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='students/images',null=True)
    address = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.user.username
    