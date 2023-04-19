from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import UUIDModel


class FunctionalMaintainers(UUIDModel):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True
    )

    class Meta:
        db_table = "functional_maintainers"
