from django.urls import path
from .views import DependenciesAPIView, DependencyAPIView

app_name = "dependencies"

urlpatterns = [
    path('', DependenciesAPIView.as_view(),
        name='create'),
    path('<pk>', DependencyAPIView.as_view(),
        name='retrieve'),
]
