from django.urls import path
from .views import TechnicalMaintainersAPIView, TechnicalMaintainerAPIView

app_name = "tmaintainers"

urlpatterns = [
    path('', TechnicalMaintainersAPIView.as_view(),
        name='create'),
    path('<pk>', TechnicalMaintainerAPIView.as_view(),
        name='retrieve'),
]
