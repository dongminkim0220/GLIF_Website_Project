from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'name_en', 'name_kr', 'profile_img', 'birthdate','phonenumber', 'year_in_school', 'workplace', 'self_intro', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'name_en', 'name_kr', 'profile_img', 'birthdate','phonenumber', 'year_in_school', 'workplace', 'self_intro', )
