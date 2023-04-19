from django.db import models
from utils.base_model import UUIDModel
from django.utils.translation import gettext_lazy as _

from functional_maintainers.models import FunctionalMaintainers
from technical_maintainers.models import TechnicalMaintainers
from dependencies.models import Dependencies
from technology.models import Technologies

class GeneralInfo(UUIDModel):
    project_name = models.CharField(max_length=150, null=False, unique=True)
    technical_maintainer = models.ForeignKey(TechnicalMaintainers, on_delete=models.SET_NULL, null=True)
    functional_maintainer = models.ForeignKey(FunctionalMaintainers, on_delete=models.SET_NULL, null=True)
    technology = models.ManyToManyField(Technologies, verbose_name=_("tech_apps"), blank=True)
    dependencies = models.ManyToManyField(Dependencies, verbose_name=_("dependency_apps"), blank=True)

    class Meta:
        db_table = 'general_info'
