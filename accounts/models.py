from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    ADDRESS_MAX_LENGTH = 100
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)

    def __str__(self):
        return self.user.username