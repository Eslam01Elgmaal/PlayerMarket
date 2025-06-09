from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    addris = models.CharField(max_length= 70)
    phone_number = models.CharField(max_length= 20)
    imge = models.ImageField(upload_to='users/')
    email = models.EmailField(max_length=254)
    facebook = models.URLField(max_length=200,blank=True,null=True,)
    x = models.URLField(max_length=200,blank=True,null=True,)
    instgram = models.URLField(max_length=200,blank=True,null=True,)
    youtube = models.URLField(max_length=200,blank=True,null=True,)
    descrabtion = models.CharField(max_length= 70)

    def __str__(self):
        return self.user.username
    

