from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.fields.related import ForeignKey
from django.utils.html import linebreaks
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
   
    @classmethod        
    def update_profile(cls, id, profile):
        cls.objects.filter(id=id).update(profile=profile)

class Image(models.Model):
    image = CloudinaryField('posts')
    image_name= models.CharField(max_length=50, blank=True)
    image_caption= models.CharField(max_length=400)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=30,blank=True)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)  
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()   

    @property
    def comments(self):
        return self.comments.all()

    def likes(self):
        return self.likes.count()
              