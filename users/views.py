from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegistration, UserUpdate, ProfileUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        register_form = UserRegistration(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            redirect('market-home')
    else:
        register_form = UserRegistration()
    context = {
        'form' : register_form
    }
    return render(request, 'users/register.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('market-home')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance = request.user)
        p_form = ProfileUpdate(request.POST, request.FILES, 
                                instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdate(instance = request.user)
        p_form = ProfileUpdate()
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)