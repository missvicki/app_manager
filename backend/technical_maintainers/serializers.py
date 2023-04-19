from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import TechnicalMaintainers


class TechnicalMSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Technical Maintainers objects."""

    class Meta:
        model = TechnicalMaintainers
        fields = (
            "id",
            "name"
        )


class PostTechnicalMSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Technical Maintainers objects."""

    class Meta:
        model = TechnicalMaintainers
        fields = (
            "name",
        )
