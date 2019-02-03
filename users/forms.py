from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Glifer, Applicant, Subject

from django.db import transaction

class GliferSignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length = 250)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_glifer = True
        # user.email.add(*self.cleaned_data.get('email'))
        user.save()
        glifer = Glifer.objects.create(user=user)
        return user

class ApplicantSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email']
        
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
        exclude = ['user', 'is_authorized']
        

class ApplicantEditForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'
        exclude = ['user',]

    havetaken_courses = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    willtake_courses = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
