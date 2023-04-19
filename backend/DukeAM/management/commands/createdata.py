import random

from django.db import transaction
from django.core.management.base import BaseCommand

from dependencies.models import Dependencies
from functional_maintainers.models import FunctionalMaintainers
from technical_maintainers.models import TechnicalMaintainers
from DukeAM.models import GeneralInfo
from technology.models import Technologies
from data.factories import (
    DependenciesFactory,
    FunctionalMaintainersFactory,
    TechnicalMaintainersFactory,
    TechnologiesFactory,
    GeneralInfoFactory,
)

NO_APPS = 100
NO_TECH = 10
NO_DEP = 10
NO_TECHM = 5
NO_FUNCM = 5


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # self.stdout.write("Deleting old data...")
        # models = [User, Thread, Comment, Club]
        # for m in models:
        #     m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # create technologies
        tech = []
        for _ in range(NO_TECH):
            techn = TechnologiesFactory()
            tech.append(tech)
        # create dependencies
        dependen = []
        for _ in range(NO_TECH):
            dep = DependenciesFactory()
            dependen.append(dep)

        # create technical maintainer
        tecmain = []
        for _ in range(NO_TECHM):
            tecm = TechnicalMaintainersFactory()
            tecmain.append(tecm)

        # create functional maintainer
        funcmain = []
        for _ in range(NO_FUNCM):
            funm = FunctionalMaintainersFactory()
            funcmain.append(funm)

        # Create all the apps
        apps = []
        for _ in range(NO_APPS):
            technical_maintainer = random.choice(tecmain)
            functional_maintainer = random.choice(funcmain)
            technology = random.choice(tech)
            print(technology)
            # dependencies = random.choice(dependen)
            # app = GeneralInfoFactory(
            #     functional_maintainer=functional_maintainer,
            #     technical_maintainer=technical_maintainer,
            #     technology=technology,
            #     dependencies=dependencies
            # )
            # apps.append(app)
