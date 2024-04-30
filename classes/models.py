from django.db import models
from course.models import Course

# Create your models here.
class Contents(models.Model):
    class_name = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    upload_at = models.DateTimeField( auto_now_add=True)
    def __str__(self):
        return f"{self.course.name}/{self.class_name}"