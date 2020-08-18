from django.db import models


class Formation(models.Model):
    """Formation object"""
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    time = models.IntegerField()
    jobID = models.IntegerField()

    def __str__(self):
        return self.name


class Artisan(models.Model):
    """Artisan object"""
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    jobID = models.IntegerField()

    def __str__(self):
        return self.name
