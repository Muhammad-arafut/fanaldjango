from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):

    return render (request, 'frontend/index.html')

def about(request):
    return render (request, 'frontend/about.html')

def activity(request):
    return render (request, 'frontend/activity.html')

def contact(request):
    return render (request, 'frontend/contact.html')

def sign_up(request):
    return render (request, 'frontend/sign_up.html')
