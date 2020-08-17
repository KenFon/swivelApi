from unittest.mock import patch

from django.test import TestCase

from core import models


class ModelTest(TestCase):

    def test_formation_str(self):
        """Test the formation string representation"""
        formation = models.Formation.objects.create(
            name="Formation Simplon",
            lieu="MDNI",
            time=5
        )

        self.assertEqual(str(formation), formation.name)
