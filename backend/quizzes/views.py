from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.db.models import Prefetch

from .models import Quiz, Question
from .serializers import QuizSerializer


class QuizViewSet(ModelViewSet):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Quiz.objects.select_related("category", "creator").prefetch_related(
            "tags",
            Prefetch(
                "questions",
                queryset=Question.objects.prefetch_related("options")
            )
        )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)