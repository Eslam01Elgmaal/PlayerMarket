from django.contrib import admin
from .models import About
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_title')  # عرض الحقول في القائمة
    list_filter = ('job_title',)  # إضافة فلتر حسب الوظيفة
    search_fields = ('name', 'email')  # البحث بالاسم أو الإيميل