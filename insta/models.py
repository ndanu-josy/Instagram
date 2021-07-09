from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profilesss')
    bio = models.CharField(max_length=50)