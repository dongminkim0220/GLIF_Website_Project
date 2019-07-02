from django.shortcuts import render
from .models import Recruiting
from django.views.generic import DetailView

# Create your views here.
def index(request):
    recruiting = Recruiting.objects.get(pk = 1)
    return render(request, 'recruiting/index.html', {'recruiting': recruiting})