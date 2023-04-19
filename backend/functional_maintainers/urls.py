from django.urls import path
from .views import FunctionalMaintainersAPIView, FunctionalMaintainerAPIView

app_name = "fmaintainers"

urlpatterns = [
    path('', FunctionalMaintainersAPIView.as_view(),
        name='create'),
    path('<pk>', FunctionalMaintainerAPIView.as_view(),
        name='retrieve'),
]
