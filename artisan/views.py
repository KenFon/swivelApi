from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Artisan
from artisan import serializers


class ArtisanViewSet(viewsets.ModelViewSet):
    """Manage formations in the database"""
    serializer_class = serializers.ArtisanSerializer
    queryset = Artisan.objects.all()

    def get_queryset(self):
        return self.queryset
