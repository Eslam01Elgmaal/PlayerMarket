from django.contrib import admin
from .models import TShirt

# Register your models here.
@admin.register(TShirt)

class SuppliesAdmin(admin.ModelAdmin):
    supp = ('name', 'price', 'code', )


