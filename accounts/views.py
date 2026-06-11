from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


from .models import Profile, Follow
from django.contrib.auth.models import User

from .forms import RegisterForm



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('home')

    else:
        form = RegisterForm()


    return render(request, 'accounts/register.html', {'form': form})

def user_profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    profile, created = Profile.objects.get_or_create(user=profile_user)

    videos = profile_user.videos.all().order_by('-created_at')

    is_following = False

    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()

    return render(request, 'accounts/user_profile.html', {'profile_user': profile_user, 'videos': videos, 'profile': profile, 'is_following': is_following})


@login_required
def follow_view(request, user_id):
    target = get_object_or_404(User, id=user_id)

    if target == request.user:
        return redirect('user_profile_view', user_id=user_id)

    follow = Follow.objects.filter(follower=request.user, following=target).first()

    if follow:
        follow.delete()

    else:
        Follow.objects.create(follower=request.user, following=target)

    return redirect('user_profile', user_id=user_id)