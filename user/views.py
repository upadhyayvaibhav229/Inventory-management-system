from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm, userupdateform, profileupdateform

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()

    context = {
        'form':form,
    }
    return render(request, 'Users/register.html',context)

def profile(request):
    return render(request, 'Users/profile.html')

def profile_updates(request):
    if request.method == 'POST':
        user_form = userupdateform(request.POST, instance = request.user)
        profile_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')

    else:
        user_form = userupdateform(instance=request.user)
        profile_form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form': profile_form,
    }
    return render(request, 'Users/profile_update.html',context)
