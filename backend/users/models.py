from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.model_utils.models import TimeStampedModel

class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']