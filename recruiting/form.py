from django import forms

class LoginForm(forms.ModelForm):
    class Meta():
        Model = Applicant
        fields = __all__

# class ApplicationForm(forms.ModelForm):
#     class Meta():
#         Model = ApplicantInfo
#         fields = __all__