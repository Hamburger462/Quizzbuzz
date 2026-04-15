from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quizzes"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="quizzes"
    )

    tags = models.ManyToManyField(Tag, blank=True, related_name="quizzes")

    is_published = models.BooleanField(default=False)

    time_per_question = models.PositiveIntegerField(
        help_text="Time limit per question in seconds",
        default=10
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Question(models.Model):
    class QuestionType(models.TextChoices):
        SINGLE = "single", "Single choice"
        MULTIPLE = "multiple", "Multiple choice"
        TRUE_FALSE = "true_false", "True/False"

    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    text = models.TextField()

    question_type = models.CharField(
        max_length=20,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE
    )

    order = models.PositiveIntegerField(
        help_text="Position of the question in the quiz"
    )

    points = models.PositiveIntegerField(default=100)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]
        unique_together = ("quiz", "order")

    def __str__(self):
        return f"{self.quiz.title} - Q{self.order}"
    
    
class AnswerOption(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options"
    )

    text = models.CharField(max_length=255)

    is_correct = models.BooleanField(default=False)

    order = models.PositiveIntegerField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["order"]