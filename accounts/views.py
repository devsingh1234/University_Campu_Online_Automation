
from mailbox import Message
from multiprocessing import AuthenticationError

from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
        else:
             return render(request, 'accounts/signup.html', { 'form': form })
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})  


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #retrieve the user from post method
            user=form.get_user()
            #now login the user
            login(request,user)
            return redirect('dashboard')
        else:
             return render(request, 'accounts/login.html', { 'form': form })
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
