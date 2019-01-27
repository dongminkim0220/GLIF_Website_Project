from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Glifer, Applicant

from django.db import transaction

class GliferSignUpForm(UserCreationForm):
    # test = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_glifer = True
        user.save()
        glifer = Glifer.objects.create(user=user)
        return user

class ApplicantSignUpForm(UserCreationForm):
    # test = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_applicant = True
        user.save()
        applicant = Applicant.objects.create(user=user)
        return user

class GliferCreateForm(forms.ModelForm):
    class Meta:
        model = Glifer
        fields = '__all__'

class GliferEditForm(forms.ModelForm):
    class Meta:
        model = Glifer
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    pass


class CustomUserChangeForm(UserChangeForm):
    pass    