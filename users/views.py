from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegistration

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