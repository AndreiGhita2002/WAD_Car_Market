from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

User._meta.get_field('email')._unique = True


class UserProfile(models.Model):
    ADDRESS_MAX_LENGTH = 100
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(default="profile1.jpg", null=True)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH, unique=False)

    def __str__(self):
        return self.user.username
    
#user model is taken from django mode, Userprofile is connected to the actual user model.
    
