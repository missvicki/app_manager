from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Dependencies

class DependenciesSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Dependencies objects."""

    class Meta:
        model = Dependencies
        fields = (
            "id",
            "name"
        )


class PostDependenciesSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Dependencies objects."""

    class Meta:
        model = Dependencies
        fields = (
            "name",
        )
