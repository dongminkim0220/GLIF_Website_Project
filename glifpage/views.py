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
    return render(request, 'glifpage/announcement/announcement.html', {})

def daily(request):
    if request.META['PATH_INFO'] == '/daily/overview' :
        return render(request, 'glifpage/daily/overview.html', {})
    elif request.META['PATH_INFO'] == '/daily/newsclipping' :
        return render(request, 'glifpage/daily/clip/clip.html', {})
    elif request.META['PATH_INFO'] == '/daily/newsclipping/new' :
        return render(request, 'glifpage/daily/clip/new.html', {})
    elif request.META['PATH_INFO'] == '/daily/market' :
        return render(request, 'glifpage/daily/market/market.html', {})
    elif request.META['PATH_INFO'] == '/daily/market/new' :
        return render(request, 'glifpage/daily/market/new.html', {})

def inDepthAnalysis(request):
    return render(request, 'glifpage/inDepthAnalysis/inDepthAnalysis.html', {})

def recruiting(request):
    if request.META['PATH_INFO'] == '/recruiting' :
        return render(request, 'glifpage/recruiting/recruiting.html', {})
    elif request.META['PATH_INFO'] == '/recruiting/new' :
        return render(request, 'glifpage/recruiting/new.html', {})

def gliferOnly(request):
    if request.META['PATH_INFO'] == '/gliferonly/review' :
        return render(request, 'glifpage/gliferOnly/review.html', {})
    elif request.META['PATH_INFO'] == '/gliferonly/admin' :
        return render(request, 'glifpage/gliferOnly/admin.html', {})
