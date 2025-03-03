from django.contrib import admin
from .models import Players

# تسجيل Players موديل في الإدارة
@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = ('name', 'imge', 'club_name', 'phone_numper', 'email', 'date_from_year', 'date_to_year')  # الحقول التي ستظهر في القائمة
    search_fields = ('name', 'club_name', 'email')  # يمكنك البحث باستخدام الاسم أو النادي أو البريد الإلكتروني
    list_filter = ('club_name',)  # تصفية اللاعبين حسب النادي
    ordering = ('-date_from',)  # ترتيب اللاعبين حسب تاريخ البداية

    # تخصيص طريقة عرض الحقول في صفحة التفاصيل
    fieldsets = (
        (None, {
            'fields': ('name','imge', 'club_name', 'phone_numper', 'email', 'video')
        }),
        ('Career Info', {
            'fields': ('date_from', 'description', 'languages', 'language_strength')
        }),
        ('Skills', {
            'fields': ('dribbling', 'passing', 'shooting', 'tackling')
        }),
        ('Location', {
            'fields': ('addres',)
        }),
        ('Last Club', {
            'fields': ('last_club_name', 'date_from_year','date_to_year', 'description_lastclub')
        }),
        ('Academy Data', {
            'fields': ('academy_name', 'date_from_academy', 'date_to_academy', 'description_academy' )
        }),
         ('School Data', {
            'fields': ('school_name', 'date_from_school', 'date_to_school', 'description_school')
        }),
        
    )
