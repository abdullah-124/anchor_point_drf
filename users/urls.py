from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('list', views.Userview)

urlpatterns = [
    path('',include(router.urls)),
    path('registration/', views.RegestrationApi_view.as_view(), name='register'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    path('active/<uid64>/<token>/',views.activate,name='active')
]
