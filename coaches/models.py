from django.db import models
from django.urls import reverse


# Create your models here.

class Coaches(models.Model):
    Coaches_CHOICES = [
        ('TEC', 'Technical director'),
        ('SPO', 'Sports director'),
        ('ASS', 'Assistant coach'),
    ]
    imge = models.ImageField(upload_to='Coaches/')
    name = models.CharField(max_length=100)
    Descraption =  models.CharField(max_length=50000)
    job_title = models.CharField(max_length=3, choices=Coaches_CHOICES)

    def get_absolute_url(self):
        return reverse('coaches:coach-detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.name} - {self.get_job_title_display()}"