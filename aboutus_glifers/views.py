from django.shortcuts import render, get_object_or_404
from users.models import CustomUser, Glifer
from django.views.generic import ListView, DetailView

# Create your views here.

# class GliferList(ListView):
#     template_name = "aboutus_glifers/index.html"
#     context_object_name = "glifers"
#     model = CustomUser

#     def get_queryset(self):
#         qs = super(GliferList, self).get_queryset()
#         return qs.filter(year_in_school__exact=self.kwargs['nth'])
    
class GliferList(ListView):
    template_name = "aboutus_glifers/index.html"
    context_object_name = "glifers"
    model = Glifer

    def get_queryset(self):
        qs = super(GliferList, self).get_queryset()
        return qs.filter(nth__exact=self.kwargs['nth'])
