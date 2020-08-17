from django.db import models


class Formation(models.Model):
    """Formation object"""
    name = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    time = models.IntegerField()

    def __str__(self):
        return self.name
