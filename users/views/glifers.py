from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


from ..forms import GliferSignUpForm, GliferEditForm
from ..models import CustomUser, Glifer 

class GliferSignUpView(CreateView):
    model = CustomUser
    form_class = GliferSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'glifer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class GliferEditView(UpdateView):
    model = Glifer
    form_class = GliferEditForm
    context_object_name = 'glifer'
    template_name = 'detail/glifer-edit.html'
    success_url = reverse_lazy('home')
