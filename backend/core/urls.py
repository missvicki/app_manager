"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Duke App Manager",
        default_version="v1",
        description="Backend Documentation",
    ),
    url=settings.CURRENT_SITE,
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    path("admin/", admin.site.urls),
    path("apps/", include("DukeAM.urls", namespace="dukeam")),
    path("technology/", include("technology.urls", namespace="tech")),
    path("functional_maintainers/", include("functional_maintainers.urls", namespace="fmaintainers")),
    path("technical_maintainers/", include("technical_maintainers.urls", namespace="tmaintainers")),
    path("dependencies/", include("dependencies.urls", namespace="dependencies")),
]
