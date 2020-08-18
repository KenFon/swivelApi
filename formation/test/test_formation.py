import tempfile
import os

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Formation

from formation.serializers import FormationSerializer

FORMATION_URL = reverse('formation:formation-list')


def sample_formation(**params):
    """Create and return a sample formation"""
    defaults = {
        'name': 'Sample recipe',
        'time': 10,
        'place': 'MDNI',
        'jobID': 5
    }
    defaults.update(params)

    return Formation.objects.create(**defaults)


class PublicRecipeTest(TestCase):
    """Test unauthenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_formations(self):
        """Test retrieving a list of formation"""
        sample_formation()
        res = self.client.get(FORMATION_URL)
        formations = Formation.objects.all().order_by('-id')
        serializer = FormationSerializer(formations, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
