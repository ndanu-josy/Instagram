from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.

def index(request):
        return render(request, 'index.html')

