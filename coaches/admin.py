from django.contrib import admin
from .models import Coaches
# Register your models here.

@admin.register(Coaches)
class CoacheAdmin(admin.ModelAdmin):

    list_display = ('name', 'Descraption','imge' , 'job_title')  # عرض الحقول في القائمة
    list_filter = ('job_title',)  # إضافة فلتر حسب الوظيفة
    search_fields = ('name', 'email')  # البحث بالاسم أو الإيميل