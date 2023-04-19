from rest_framework import serializers

from .models import GeneralInfo
from technical_maintainers.serializers import TechnicalMSerializer
from functional_maintainers.serializers import FunctionalMSerializer
from dependencies.serializers import DependenciesSerializer
from technology.serializers import TechnologiesSerializer


class AppsSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of GeneralInfo objects."""
    technical_maintainer = TechnicalMSerializer(many=False, read_only=True,)
    functional_maintainer = FunctionalMSerializer(many=False, read_only=True,)
    dependencies = DependenciesSerializer(many=True, read_only=True,)
    technology = TechnologiesSerializer(many=True, read_only=True,)

    class Meta:
        model = GeneralInfo
        fields = (
            "id",
            "project_name",
            "technical_maintainer",
            "functional_maintainer",
            "technology",
            "dependencies",
        )


class PostAppsSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of GeneralInfo objects."""
    class Meta:
        model = GeneralInfo
        fields = (
            "project_name",
            "technical_maintainer",
            "functional_maintainer",
            "technology",
            "dependencies",
        )
