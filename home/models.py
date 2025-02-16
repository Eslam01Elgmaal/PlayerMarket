from django.db import models

# Create your models here.


class Home(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    intro_desc = models.CharField(max_length=1000)
    descraption = models.CharField(max_length=75)
    email = models.EmailField(max_length=254)
    addres = models.CharField(max_length=120)
    phone_numper = models.CharField(max_length=22)

    facebook = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username



class Why(models.Model):
    titel = models.CharField(max_length=70)
    desc_why = models.CharField(max_length=500)
