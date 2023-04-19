from django.urls import path
from .views import AppsAPIView, AppAPIView

app_name = "dukeam"

urlpatterns = [
    path("create-get", AppsAPIView.as_view(), name="create-get-all"),
    path("<pk>", AppAPIView.as_view(), name="retrieve"),
]
