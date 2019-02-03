from django.shortcuts import render, get_object_or_404
from users.models import CustomUser, Glifer, Nth
from django.views.generic import ListView, DetailView

# Create your views here.

    
class GliferList(ListView):
    template_name = "aboutus_glifers/index.html"
    context_object_name = "glifers"
    model = Glifer

    def get_queryset(self):
        qs = super(GliferList, self).get_queryset()
        nth_id = Nth.objects.filter(nth = self.kwargs['nth'])[0].id
        return qs.filter(nth_id__exact = nth_id )
