from django.contrib import admin
from .models import TShirt, Size, Order


class TShirtAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'code')
    list_filter = ('size',)
    search_fields = ('name', 'code')
    filter_horizontal = ('size',)


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'tshirt',
        'size',
        'price',
        'customer_phone',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'size',
        'created_at',
    )

    search_fields = (
        'customer_name',
        'customer_email',
        'customer_phone',
        'tshirt__name',
    )

    readonly_fields = (
        'price',
        'created_at',
    )

    ordering = ('-created_at',)


admin.site.register(TShirt, TShirtAdmin)
admin.site.register(Size)
admin.site.register(Order, OrderAdmin)