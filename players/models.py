from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=75)
    imge = models.ImageField(upload_to='players/')
    addres = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    phone_numper = models.CharField(max_length=22)
    club_name = models.CharField(max_length=50)
    date_from = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=20000)
    dribbling = models.IntegerField(validators=[MaxValueValidator(100)])
    passing = models.IntegerField(validators=[MaxValueValidator(100)])
    shooting = models.IntegerField(validators=[MaxValueValidator(100)])
    tackling = models.IntegerField(validators=[MaxValueValidator(100)])
    languages = models.TextField(max_length=50)
    language_strength = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    last_club_name = models.CharField(max_length=50)

    # هنا هضيف المتغيرات المطلوبة
    date_from_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),  # لا يقبل السنة قبل 1990
        ]
    )

    date_to_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990),  # لا يقبل السنة قبل 1990
        ]
    )

    def clean(self):
        """تطبيق الفاليديشن عند حفظ الموديل"""
        if self.date_to_year < self.date_from_year:
            raise ValidationError({"date_to_year": "سنة النهاية يجب أن تكون أكبر أو مساوية لسنة البداية."})

    description_lastclub = models.TextField(max_length=3000, null=True, blank=True)


    
    academy_name = models.CharField(max_length=100, null=True, blank=True)
    date_from_academy = models.IntegerField( null=True, blank=True)
    date_to_academy = models.IntegerField( null=True, blank=True)
    description_academy = models.TextField(max_length=3000, null=True, blank=True)
    

    school_name = models.CharField(max_length=100, null=True, blank=True)
    date_from_school = models.IntegerField(null=True, blank=True)
    date_to_scshool = models.IntegerField(null=True, blank=True)
    description_school = models.TextField(max_length=3000, null=True, blank=True)

    video = models.FileField(upload_to='players_videos/', null=True, blank=True)







