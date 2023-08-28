from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',]
    list_filter = ('email', 'username',)
    search_fields = ('email',)