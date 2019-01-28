from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from ..forms import ApplicantSignUpForm, ApplicantCreateForm, ApplicantEditForm
from ..models import CustomUser, Applicant 

class ApplicantSignUpView(CreateView):
    model = CustomUser
    form_class = ApplicantSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'applicants'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/recruiting')

class ApplicantEditView(UpdateView):
    model = Applicant
    form_class = ApplicantEditForm
    context_object_name = 'applicant'
    template_name = 'detail/applicant-edit.html'
    success_url = reverse_lazy('recruiting-index')