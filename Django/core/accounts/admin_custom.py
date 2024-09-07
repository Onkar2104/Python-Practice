# from django.contrib import admin

# # Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(User, UserAdmin)
