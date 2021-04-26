from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['p1']==request.POST['p2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], request.POST['p1'])
                auth.login(request, user)
                return redirect('home')
        else:return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
            
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['p1'])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:return render(request, 'accounts/login.html', {'error':'Please check the credentials and try again.'})

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')