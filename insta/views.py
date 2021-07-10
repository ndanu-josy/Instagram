from insta.models import Profile
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, profileForm, userForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
        return render(request, 'index.html')

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 


@login_required(login_url='/accounts/login/')
def profile(request):
    
    if request.method == 'POST':
        user_form = userForm(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:        
        profile_form = profileForm(instance=request.user)
        user_form =userForm(instance=request.user)
        params = {
            'update_form':user_form,
            'profile_form': profile_form
        }

    profile = Profile.objects.filter(user = request.user)    
    return render(request,'user_profile.html',{"profile":profile}) 


 