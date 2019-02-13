from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..forms import ApplicantSignUpForm, ApplicantEditForm
from ..models import CustomUser, Applicant 

# Auth
from users.decorator import glifer_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin

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

@method_decorator([login_required, glifer_required], name='dispatch')
class ApplicantListView(ListView):
    model = Applicant
    template_name = 'recruiting/list.html'
    context_object_name = 'applicants'

class ApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'recruiting/detail.html'
    context_object_name = 'applicant'
