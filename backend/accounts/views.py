# accounts/views.py

from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


class MeView(RetrieveAPIView):
    """
    Returns the authenticated user's profile.
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class UpdateMeView(UpdateAPIView):
    """
    Allows user to update profile fields (not Firebase identity).
    """

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        # Prevent changing protected fields
        request.data.pop("firebase_uid", None)
        return super().update(request, *args, **kwargs)


class BecomeHostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        if user.is_host:
            return Response(
                {"detail": "Already a host."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.is_host = True
        user.save(update_fields=["is_host"])

        return Response({"is_host": True})