from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('profiles-pic')
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,blank=True,related_name='follow')

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete() 

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
