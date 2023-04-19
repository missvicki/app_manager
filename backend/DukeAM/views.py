from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,)
from rest_framework.response import Response
from rest_framework import status

from .serializers import AppsSerializer, PostAppsSerializer
from DukeAM.models import GeneralInfo


class AppsAPIView(
    ListModelMixin,
    GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = GeneralInfo.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = PostAppsSerializer

    def post(self, request):
        """
        Method to handle post requests for creating a apps
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        apps:- the app data created by a user.
        endpoints.
        """
        serializer_class = AppsSerializer
        app = request.data.get(
            'apps', {}) if 'apps' in request.data else request.data

        serializer = self.serializer_class(data=app)
        serializer.is_valid(raise_exception=True)
        new_app = serializer.save()

        resp_data = serializer_class(new_app).data

        return Response(resp_data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving apps
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        app:- the app data retrieved by a user.
        endpoints.
        """
        self.serializer_class = AppsSerializer
        return self.list(request, *args, **kwargs)
        
class AppAPIView(
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericAPIView):
    # Allow any authenticated user to hit this endpoint.
    queryset = GeneralInfo.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AppsSerializer

    def get(self, request, *args, **kwargs):
        """
        Method to handle gwt requests for retrieving a app
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        app:- the app data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a app
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        app:- the app data updated by a user.
        endpoints.
        """        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a app
        """        
        return self.destroy(request, *args, **kwargs)
