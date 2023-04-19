from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Technologies

class TechnologiesSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Technologies objects."""

    class Meta:
        model = Technologies
        fields = (
            "id",
            "tech_name"
        )


class PostTechnologiesSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Technologies objects."""

    class Meta:
        model = Technologies
        fields = (
            "tech_name",
        )
