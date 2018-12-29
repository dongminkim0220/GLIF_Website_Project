from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'glifpage/index.html', {})

def aboutUs(request):
    if request.META['PATH_INFO'] == '/aboutus/introduction' :
        return render(request, 'glifpage/aboutUs/introduction.html', {})
    elif request.META['PATH_INFO'] == '/aboutus/glifers' :
        return render(request, 'glifpage/aboutUs/glifers.html', {})

def announcement(request):
    return render(request, 'glifpage/announcement.html', {})

def daily(request):
    return render(request, 'glifpage/daily.html', {})

def inDepthAnalysis(request):
    return render(request, 'glifpage/inDepthAnalysis.html', {})

def recruiting(request):
    return render(request, 'glifpage/recruiting.html', {})