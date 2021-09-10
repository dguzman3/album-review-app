from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import CustomUser

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=2, decimal_places=1, 
        validators=[MaxValueValidator(10.0), MinValueValidator(0.0)])
    text = models.TextField()
