from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    image = models.ImageField(upload_to='category/images',null=True)
    def __str__(self) -> str:
        return self.category_name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='course/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.IntegerField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=40, null=True)
    fee = models.IntegerField(null=True)
    mobile_num = models.CharField(max_length=12,)

    def __str__(self) -> str:
        return f"{self.name} by {self.teacher.user.username}"

STAR_REVIEW = (
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
)
class Reviews(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    review = models.TextField(null = True)
    star = models.CharField(max_length=5, choices=STAR_REVIEW)

class Enroll(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12)
    date_of_enroll = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.course.name}/{self.student}"