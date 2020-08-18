from unittest.mock import patch

from django.test import TestCase

from core import models


class ModelTest(TestCase):

    def test_formation_str(self):
        """Test the formation string representation"""
        formation = models.Formation.objects.create(
            name="Formation Simplon",
            place="MDNI",
            time=5,
            jobID=3,
        )

        self.assertEqual(str(formation), formation.name)

    def test_artisan_str(self):
        """Test the artisan string representation"""
        formation = models.Artisan.objects.create(
            name="Momo le boucher",
            place="Le place de la bastille",
            jobID=5
        )

        self.assertEqual(str(formation), formation.name)
