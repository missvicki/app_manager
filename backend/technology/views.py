from django.shortcuts import render
from technology.models import Technologies
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

from .serializers import TechnologiesSerializer, PostTechnologiesSerializer


class TechnologiesAPIView(ListModelMixin, GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = Technologies.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostTechnologiesSerializer

    def post(self, request):
        """
        Method to handle post requests for creating a technology
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technology:- the technology data created by a user.
        endpoints.
        """
        serializer_class = TechnologiesSerializer
        technology = (
            request.data.get("technology", {})
            if "technology" in request.data
            else request.data
        )

        serializer = self.serializer_class(data=technology)
        serializer.is_valid(raise_exception=True)
        new_technology = serializer.save()

        resp_data = serializer_class(new_technology).data

        return Response(resp_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving tecnhologies
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technology:- the technology data retrieved by a user.
        endpoints.
        """
        self.serializer_class = TechnologiesSerializer
        return self.list(request, *args, **kwargs)


class TechnologyAPIView(
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    # Allow any authenticated user to hit this endpoint.
    queryset = Technologies.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TechnologiesSerializer

    def get(self, request, *args, **kwargs):
        """
        Method to handle gwt requests for retrieving a technology
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technology:- the technology data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a technology
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technology:- the technology data updated by a user.
        endpoints.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a technology
        """
        return self.destroy(request, *args, **kwargs)
