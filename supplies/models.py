import random
from django.db import models

# Create your models here.



class TShirt(models.Model):
    Size_CHOICES = [
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imge = models.ImageField(upload_to='supplies/')
    size = models.CharField(max_length=4, choices=Size_CHOICES)
    code = models.CharField(max_length=4, unique=True, editable=False)

    

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = str(random.randint(1000, 9999))  # يولد رقم من 4 أرقام
            if not TShirt.objects.filter(code=code).exists():
                return code

    def __str__(self):
        return f"{self.name} - {self.code}"

    def __str__(self):
        return f"{self.name} - {self.get_size_display()}"
