from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'age', 'speak_lang', 'it_lang')
    list_filter = ('speak_lang', 'it_lang')
    search_fields = ('user__username', 'user__email', 'bio')
    raw_id_fields = ('user',)  # If you want to use raw_id_fields for ForeignKey
