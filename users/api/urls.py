from django.urls import path, include
from users.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.UserViewset, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
