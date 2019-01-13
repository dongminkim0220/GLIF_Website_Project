from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'setups/index.html', {})


def login(request):
    return render(request, 'setups/login.html', {})


def signup(request):
    return render(request, 'setups/signup.html', {})