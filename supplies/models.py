import random
from django.db import models

class Size(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    name = models.CharField(max_length=2, choices=SIZE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class TShirt(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imge = models.ImageField(upload_to='supplies/')
    size = models.ManyToManyField(Size)
    code = models.CharField(max_length=4, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = str(random.randint(0, 9999)).zfill(4)  
            if not TShirt.objects.filter(code=code).exists():
                return code

    def __str__(self):
        return self.name

class Purchase(models.Model):
    tshirt = models.ForeignKey(TShirt, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.tshirt.name} - {self.size}"
