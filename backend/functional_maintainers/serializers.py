from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import FunctionalMaintainers

class FunctionalMSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Functional Maintainers objects."""

    class Meta:
        model = FunctionalMaintainers
        fields = (
            "id",
            "name"
        )


class PostFunctionalMSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of Functional Maintainers objects."""

    class Meta:
        model = FunctionalMaintainers
        fields = (
            "name",
        )
