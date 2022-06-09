from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def main(request):
    return render(request, 'main.html', {})

def single_blog(request):
    return render(request, 'single-blog.html', {})

def track(request):
    return render(request, 'track.html', {})

