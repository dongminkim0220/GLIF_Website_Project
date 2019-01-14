from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        ('Required', {
            'fields': ('username', 'email', 'name_en', 'name_kr', 'profile_img', 'birthdate','phonenumber', 'year_in_school', 'workplace', 'self_intro', )
        }),
    )
    list_display = ('username', 'email', 'name_en', 'name_kr', 'profile_img', 'birthdate','phonenumber', 'year_in_school', 'workplace', 'self_intro', )

admin.site.register(CustomUser, CustomUserAdmin)