from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    pass

class ReviewGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255)
    members = models.ManyToManyField(CustomUser, related_name='members')
