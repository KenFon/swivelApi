from django.urls import path, include
from rest_framework.routers import DefaultRouter

from formation import views

router = DefaultRouter()
router.register('formation', views.FormationViewSet)

app_name = 'formation'

urlpatterns = [
    path('', include(router.urls))
]
