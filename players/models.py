from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.urls import reverse


# Create your models here.

class Players(models.Model):

    POSITIONS = [
        ('GK', 'Goalkeeper'),
        ('RB', 'Right Back'),
        ('LB', 'Left Back'),
        ('CB', 'Center Back'),
        ('CD', 'Center Defense'),
        ('RM', 'Right Midfielder'),
        ('LM', 'Left Midfielder'),
        ('CM', 'Center Midfielder'),
        ('RW', 'Right Wing'),
        ('LW', 'Left Wing'),
        ('ST', 'Striker'),
        
    ]

    position = models.CharField(
        max_length=3,
        choices=POSITIONS,
        default='GK',
        verbose_name='Player Position'
    )


    country = CountryField(blank_label='(select country)')
    name = models.CharField(max_length=75)
    imge = models.ImageField(upload_to='players/')
    addres = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    phone_numper = models.CharField(max_length=22)
    club_name = models.CharField(max_length=50)
    club_flag = models.ImageField(upload_to='players/')    
    date_from = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=20000)
    dribbling = models.IntegerField(validators=[MaxValueValidator(100)])
    passing = models.IntegerField(validators=[MaxValueValidator(100)])
    shooting = models.IntegerField(validators=[MaxValueValidator(100)])
    Pace = models.IntegerField(validators=[MaxValueValidator(100)])
    Defense = models.IntegerField(validators=[MaxValueValidator(100)])
    Physical = models.IntegerField(validators=[MaxValueValidator(100)])


    over_rating = models.IntegerField(blank=True, null=True)


    def save(self, *args, **kwargs):
    # حساب over_rating
        self.over_rating = round(
            self.Pace * 0.2 +
            self.shooting * 0.25 +
            self.passing * 0.15 +
            self.dribbling * 0.2 +
            self.Defense * 0.1 +
            self.Physical * 0.1
        )

        # توليد slug لو مش موجود
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Players.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        # حفظ البيانات مرة واحدة فقط
        super().save(*args, **kwargs)




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



    slug = models.SlugField(null=True , blank=True , unique=True)

    def get_absolute_url(self):

        return reverse('players:player_detail',kwargs={'slug': self.slug}) 






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
    date_to_school = models.IntegerField(null=True, blank=True)
    description_school = models.TextField(max_length=3000, null=True, blank=True)

    video = models.FileField(upload_to='players_videos/', null=True, blank=True)







