from django.shortcuts import render
from functional_maintainers.models import FunctionalMaintainers
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

from .serializers import FunctionalMSerializer, PostFunctionalMSerializer


class FunctionalMaintainersAPIView(ListModelMixin, GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = FunctionalMaintainers.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostFunctionalMSerializer

    def post(self, request):
        """
        Method to handle post requests for creating a functional maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the functional maintainer data created by a user.
        endpoints.
        """
        serializer_class = FunctionalMSerializer
        functional_maintainer = (
            request.data.get("functional_maintainer", {})
            if "functional_maintainer" in request.data
            else request.data
        )

        serializer = self.serializer_class(data=functional_maintainer)
        serializer.is_valid(raise_exception=True)
        new_functional_maintainer = serializer.save()

        resp_data = serializer_class(new_functional_maintainer).data

        return Response(resp_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving functional maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the functional maintainer data retrieved by a user.
        endpoints.
        """
        self.serializer_class = FunctionalMSerializer
        return self.list(request, *args, **kwargs)


class FunctionalMaintainerAPIView(
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView
):
    # Allow any authenticated user to hit this endpoint.
    queryset = FunctionalMaintainers.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = FunctionalMSerializer

    def get(self, request, *args, **kwargs):
        """
        Method to handle gwt requests for retrieving a functional maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the functional maintainer data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a functional maintainer
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        functional_maintainer:- the functional maintainer data updated by a user.
        endpoints.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a functional maintainer
        """
        return self.destroy(request, *args, **kwargs)
