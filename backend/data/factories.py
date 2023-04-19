import factory
import factory.fuzzy

from dependencies.models import Dependencies
from functional_maintainers.models import FunctionalMaintainers
from technical_maintainers.models import TechnicalMaintainers
from DukeAM.models import GeneralInfo
from technology.models import Technologies


class DependenciesFactory(factory.Factory):

    class Meta: 
        model = Dependencies
        # django_get_or_create = ('name',)
    
    name = factory.Faker("name")


class FunctionalMaintainersFactory(factory.Factory):

    class Meta: 
        model = FunctionalMaintainers
        # django_get_or_create = ('name',)
    
    name = factory.Faker("name")


class TechnicalMaintainersFactory(factory.Factory):

    class Meta: 
        model = TechnicalMaintainers
        # django_get_or_create = ('name',)
    
    name = factory.Faker("name")


class TechnologiesFactory(factory.Factory):

    class Meta: 
        model = Technologies
    
    tech_name = factory.fuzzy.FuzzyChoice(choices=['Python', 'JavaScript', 'Ruby', 'Java', 'Script', 'Golang', 'C', 'PHP'])


class GeneralInfoFactory(factory.Factory):

    class Meta: 
        model = GeneralInfo
        # django_get_or_create = ('project_name',)


    project_name = factory.Faker("name")
    technical_maintainer = factory.SubFactory(TechnicalMaintainersFactory)
    functional_maintainer = factory.SubFactory(FunctionalMaintainersFactory)


    @factory.post_generation
    def technology(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for tech in extracted:
                self.technology.add(tech)

    @factory.post_generation
    def dependencies(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for dependency in extracted:
                self.dependencies.add(dependency)
                

