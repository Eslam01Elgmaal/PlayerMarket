from django.contrib import admin
from .models import Players


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'imge', 'club_name', 'phone_numper', 'email',
        'date_from_year', 'date_to_year', 'get_position_full'  
    )
    search_fields = ('name', 'club_name', 'email')
    list_filter = ('club_name',)
    ordering = ('-date_from',)

    def get_position_full(self, obj):
        return obj.get_position_display()
    get_position_full.short_description = 'Position'

    fieldsets = (
        (None, {
            'fields': ('name', 'imge','country', 'club_name','club_flag', 'phone_numper', 'email', 'video', 'position')  
        }),
        ('Career Info', {
            'fields': ('date_from', 'description', 'languages', 'language_strength')
        }),
        ('Skills', {
            'fields': ('dribbling', 'passing', 'shooting', 'Pace', 'Defense', 'Physical',)
        }),
        ('Location', {
            'fields': ('addres',)
        }),
        ('Last Club', {
            'fields': ('last_club_name', 'date_from_year', 'date_to_year', 'description_lastclub')
        }),
        ('Academy Data', {
            'fields': ('academy_name', 'date_from_academy', 'date_to_academy', 'description_academy')
        }),
        ('School Data', {
            'fields': ('school_name', 'date_from_school', 'date_to_school', 'description_school')
        }),
    )
