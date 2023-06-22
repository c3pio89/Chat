from .views import ApiUsers, ApiRooms
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register('rooms', ApiRooms)
router.register('users', ApiUsers)
from .views import index
urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]

