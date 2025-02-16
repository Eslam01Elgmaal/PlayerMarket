from django.db import models

# Create your models here.

class About(models.Model):
    JOB_CHOICES = [
        ('CEO', 'CEO'),
        ('FOU', 'Founder'),
        ('DIR', 'Managing Director'),
    ]
    imge = models.ImageField(upload_to='About/')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=3, choices=JOB_CHOICES)


    def __str__(self):
        return f"{self.name} - {self.get_job_title_display()}"