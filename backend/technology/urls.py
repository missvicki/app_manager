from django.urls import path
from .views import TechnologiesAPIView, TechnologyAPIView

app_name = "tech"

urlpatterns = [
    path('', TechnologiesAPIView.as_view(),
        name='create'),
    path('<pk>', TechnologyAPIView.as_view(),
        name='retrieve'),
]
