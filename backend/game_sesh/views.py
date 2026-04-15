from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now

from .models import GameSession, Player, PlayerAnswer
from .serializers import GameSessionSerializer, PlayerSerializer, PlayerAnswerSerializer
from .services import push_session_update, push_players


class GameSessionViewSet(ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        session = serializer.save(host=self.request.user)
        push_session_update(session)

    def perform_update(self, serializer):
        session = serializer.save()
        push_session_update(session)


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.select_related("session")
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        player = serializer.save()
        push_players(player.session)

    def perform_update(self, serializer):
        player = serializer.save()
        push_players(player.session)

    def perform_destroy(self, instance):
        session = instance.session
        instance.delete()
        push_players(session)



class PlayerAnswerViewSet(ModelViewSet):
    queryset = PlayerAnswer.objects.all()
    serializer_class = PlayerAnswerSerializer