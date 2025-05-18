from django.contrib import admin
from .models import Home , Why 
# Register your models here.


@admin.register(Home)

class HomeAdmin(admin.ModelAdmin):
    Home_list = ('user', 'intro_desc', 'descraption', 'email', 'addres', 'phone_numper', )
    Social = ('facebook', 'x', 'instagram', 'youtube', 'linkedin', )

    choose_us = ('titel', 'desc_why', )
    


@admin.register(Why)
class WhyAdmin(admin.ModelAdmin):
    list_display = ("titel", "desc_why")