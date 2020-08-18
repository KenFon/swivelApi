from django.urls import path, include
from rest_framework.routers import DefaultRouter

from artisan import views

router = DefaultRouter()
router.register('artisan', views.ArtisanViewSet)

app_name = 'artisan'

urlpatterns = [
    path('', include(router.urls))
]
