from django.urls import path
from .views import MeView, UpdateMeView, BecomeHostView

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    path("me/update/", UpdateMeView.as_view(), name="update-me"),
    path("become-host/", BecomeHostView.as_view(), name="become-host"),
]