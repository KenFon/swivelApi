from rest_framework import serializers

from core.models import Formation


class FormationSerializer(serializers.ModelSerializer):
    """Serializer for formation objects"""

    class Meta:
        model = Formation
        fields = ('id', 'name', 'place', 'time')
        read_only_field = ('id', )
