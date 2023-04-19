from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.base_model import UUIDModel

class Dependencies(UUIDModel):
    name = models.CharField(
        max_length=150,
        null=False,
        unique=True
    )

    class Meta:
        db_table = "dependencies"
