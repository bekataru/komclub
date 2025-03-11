from django.db import models
from django.contrib.auth.models import AbstractUser
from backend.backend.model_utils.models import TimeStampedModel

class User(AbstractUser, TimeStampedModel):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']