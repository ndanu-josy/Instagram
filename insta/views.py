from django.http import request
from insta.models import Profile, Image
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, profileForm, userForm, postImageForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    profile = Profile.objects.all()
    posts = Image.objects.all()

    return render(request,'index.html',{"profile":profile, "posts":posts})
       

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
            return redirect('index')
    else:        
        profile_form = profileForm(instance=request.user)
        user_form =userForm(instance=request.user)         
    return render(request,'user_profile.html',{"user_form":user_form,"profile_form": profile_form}) 

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        user_form1 = userForm(request.POST, instance=request.user)
        profile_form1 = profileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form1.is_valid():
            user_form1.save()
            profile_form1.save()
            return redirect('profile')
    else: 
        profile_form1 = profileForm(instance=request.user)
        user_form1 = userForm(instance=request.user)
    return render(request, 'update_profile.html', {"user_form1":user_form1,"profile_form1": profile_form1})



@login_required(login_url='accounts/login/')
def post_image(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = postImageForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.cleaned_data.get('image')
            image_caption=form.cleaned_data.get('image_caption')
          
            gram = Image(image = image,image_caption= image_caption, profile=user_profile)
            gram.save_image() 
        return redirect('index')
    else:
        form = postImageForm()


    return render(request,'post_image.html', {"form": form})  


 

