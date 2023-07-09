from django.contrib import admin
from apps.users.models import UserRegister

admin.site.register(UserRegister)
# class UserAdmin(admin.ModelAdmin):