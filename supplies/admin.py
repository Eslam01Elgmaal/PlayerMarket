from django.contrib import admin
from .models import TShirt, Size, Purchase


class TShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'code',)
    list_filter = ('size',)
    search_fields = ('name',)
    filter_horizontal = ('size',)  

admin.site.register(TShirt, TShirtAdmin)
admin.site.register(Size)
admin.site.register(Purchase)
