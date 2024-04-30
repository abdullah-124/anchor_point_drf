from django.contrib import admin
from . import models
# Register your models here.
class Category_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}

admin.site.register(models.Category,Category_admin)
admin.site.register(models.Course)
admin.site.register(models.Reviews)
admin.site.register(models.Enroll)