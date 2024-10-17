from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CLASS_STANDINGS = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    class_standing = models.CharField(max_length=2, choices=CLASS_STANDINGS, default='FR')