from firebase_admin import auth
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from .models import User


class FirebaseAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        header = request.headers.get("Authorization")

        if not header or not header.startswith("Bearer "):
            return None

        token = header.split(" ")[1]

        try:
            decoded = auth.verify_id_token(token)
        except Exception:
            raise AuthenticationFailed("Invalid Firebase token")

        user = self._get_or_create_user(decoded)

        return (user, decoded)

    def _get_or_create_user(self, decoded):
        uid = decoded["uid"]

        user, _ = User.objects.get_or_create(
            firebase_uid=uid,
            defaults={
                "email": decoded.get("email"),
                "display_name": decoded.get("name", ""),
                "is_anonymous": decoded.get("firebase", {}).get("sign_in_provider") == "anonymous",
            },
        )

        return user