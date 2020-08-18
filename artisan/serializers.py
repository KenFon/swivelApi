from rest_framework import serializers

from core.models import Artisan


class ArtisanSerializer(serializers.ModelSerializer):
    """Serializer for artisan objects"""

    class Meta:
        model = Artisan
        fields = ('id', 'name', 'place')
        read_only_field = ('id', )
