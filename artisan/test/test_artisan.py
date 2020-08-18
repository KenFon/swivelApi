import tempfile
import os

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Artisan

from artisan.serializers import ArtisanSerializer

ARTISAN_URL = reverse('artisan:artisan-list')


def sample_artisan(**params):
    """Create and return a sample artisan"""
    defaults = {
        'name': 'Sample recipe',
        'place': 'Place d arme',
        'jobID': 1
    }
    defaults.update(params)

    return Artisan.objects.create(**defaults)


class PublicRecipeTest(TestCase):
    """Test unauthenticated artisan API access"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_artisan(self):
        """Test retrieving a list of artisan"""
        sample_artisan()
        res = self.client.get(ARTISAN_URL)
        artisans = Artisan.objects.all().order_by('-id')
        serializer = ArtisanSerializer(artisans, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

