from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "firebase_uid",
            "email",
            "display_name",
            "is_host",
            "is_anonymous",
            "created_at",
        ]
        read_only_fields = ["id", "firebase_uid", "created_at"]