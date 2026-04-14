from django.db import models

# Create your models here.
class User(models.Model):
    """
    Django representation of a Firebase-authenticated user.
    Works for both anonymous and registered Firebase users.
    """

    firebase_uid = models.CharField(max_length=128, unique=True)

    email = models.EmailField(null=True, blank=True, unique=True)

    display_name = models.CharField(max_length=80, blank=True)

    is_host = models.BooleanField(default=False)

    is_anonymous = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name or self.firebase_uid