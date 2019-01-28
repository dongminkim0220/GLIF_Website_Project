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

class GliferEditForm(forms.ModelForm):
    class Meta:
        model = Glifer
        fields = '__all__'

class ApplicantEditForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'

