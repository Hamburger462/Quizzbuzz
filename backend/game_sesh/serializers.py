from rest_framework import serializers
from .models import GameSession, Player, PlayerAnswer


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "nickname", "score"]
        
class GameSessionSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = GameSession
        fields = [
            "id",
            "quiz",
            "status",
            "current_question_index",
            "players",
            "created_at"
        ]
        
class PlayerAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAnswer
        fields = [
            "id",
            "player",
            "question",
            "selected_options",
            "answered_at"
        ]