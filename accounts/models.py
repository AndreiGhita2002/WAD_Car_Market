from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ADDRESS_MAX_LENGTH = 100
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(default="profile1.jpg", null=True, blank=True)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH, unique=False)

    def __str__(self):
        return self.user.username
