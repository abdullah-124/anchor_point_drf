from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    image = models.ImageField(upload_to='teacher/images/',null=True)
    description = models.TextField(null=True ,blank=True)

    def __str__(self) -> str:
        return self.user.username