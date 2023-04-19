from django.shortcuts import render
from dependencies.models import Dependencies
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework import status

from .serializers import DependenciesSerializer, PostDependenciesSerializer


class DependenciesAPIView(ListModelMixin, GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = Dependencies.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostDependenciesSerializer

    def post(self, request):
        """
        Method to handle post requests for creating a dependency
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        dependency:- the dependency data created by a user.
        endpoints.
        """
        serializer_class = DependenciesSerializer
        dependency = (
            request.data.get("dependency", {})
            if "dependency" in request.data
            else request.data
        )

        serializer = self.serializer_class(data=dependency)
        serializer.is_valid(raise_exception=True)
        new_dependency = serializer.save()

        resp_data = serializer_class(new_dependency).data

        return Response(resp_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving dependencies
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the dependencies data retrieved by a user.
        endpoints.
        """
        self.serializer_class = DependenciesSerializer
        return self.list(request, *args, **kwargs)


class DependencyAPIView(
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    # Allow any authenticated user to hit this endpoint.
    queryset = Dependencies.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = DependenciesSerializer

    def get(self, request, *args, **kwargs):
        """
        Method to handle gwt requests for retrieving a dependencies
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the dependencies data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a dependencies
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the dependencies data updated by a user.
        endpoints.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a dependencies
        """
        return self.destroy(request, *args, **kwargs)
