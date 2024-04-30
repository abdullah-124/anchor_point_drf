from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('list', views.CourseView)
router.register('category', views.CategoryView)
router.register('enroll', views.EnrollView)
router.register('reviews', views.ReviewsView)

urlpatterns = [
    path('',include(router.urls))
]
