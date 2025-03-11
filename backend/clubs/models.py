from django.db import models
from backend.model_utils.models import TimeStampedModel

class Club(TimeStampedModel):
    club_name = models.CharField(max_length=255)
    club_description = models.TextField()
    announcment = models.TextField()
    members = models.ManyToManyField('users.User', related_name='clubs')
    owner = models.ForeignKey('users.User', related_name='owned_clubs', on_delete=models.CASCADE)