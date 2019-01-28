from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import CustomUser, Glifer, Applicant

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Glifer)
admin.site.register(Applicant)
