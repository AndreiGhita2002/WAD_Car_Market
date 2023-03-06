from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')

def contact_us(request):
    return render(request, 'core/contact_us.html')

def about_us(request):
    return render(request, 'core/about_us.html')
