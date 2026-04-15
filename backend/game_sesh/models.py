from django.db import models
from django.contrib.auth import get_user_model
from quizzes.models import Quiz, Question, AnswerOption

User = get_user_model()


class GameSession(models.Model):
    class Status(models.TextChoices):
        WAITING = "waiting", "Waiting"
        ACTIVE = "active", "Active"
        FINISHED = "finished", "Finished"

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="sessions"
    )

    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="hosted_sessions"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.WAITING
    )

    current_question_index = models.PositiveIntegerField(default=0)

    started_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session {self.id} ({self.quiz.title})"
    
    
class Player(models.Model):
    session = models.ForeignKey(
        GameSession,
        on_delete=models.CASCADE,
        related_name="players"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    nickname = models.CharField(max_length=50)

    score = models.IntegerField(default=0)

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
    
class PlayerAnswer(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )

    selected_options = models.ManyToManyField(AnswerOption)

    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("player", "question")