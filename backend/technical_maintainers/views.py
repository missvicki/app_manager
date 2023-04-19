from django.shortcuts import render
from technical_maintainers.models import TechnicalMaintainers
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

from .serializers import TechnicalMSerializer, PostTechnicalMSerializer


class TechnicalMaintainersAPIView(ListModelMixin, GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = TechnicalMaintainers.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostTechnicalMSerializer

    def post(self, request):
        """
        Method to handle post requests for creating a Technical maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technical_maintainer:- the Technical maintainer data created by a user.
        endpoints.
        """
        serializer_class = TechnicalMSerializer
        technical_maintainer = (
            request.data.get("technical_maintainer", {})
            if "technical_maintainer" in request.data
            else request.data
        )

        serializer = self.serializer_class(data=technical_maintainer)
        serializer.is_valid(raise_exception=True)
        new_technical_maintainer = serializer.save()

        resp_data = serializer_class(new_technical_maintainer).data

        return Response(resp_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving technical maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technical_maintainer:- the technical maintainer data retrieved by a user.
        endpoints.
        """
        self.serializer_class = TechnicalMSerializer
        return self.list(request, *args, **kwargs)


class TechnicalMaintainerAPIView(
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    # Allow any authenticated user to hit this endpoint.
    queryset = TechnicalMaintainers.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TechnicalMSerializer

    def get(self, request, *args, **kwargs):
        """
        Method to handle gwt requests for retrieving a technical maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technical_maintainer:- the technical maintainer data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a technical maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        technical_maintainer:- the technical maintainer data updated by a user.
        endpoints.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a technical maintainer
        """
        return self.destroy(request, *args, **kwargs)
