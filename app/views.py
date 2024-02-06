from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SigUpForm


def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticated
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been logged In")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Login in Please Tre Again ...")
            return redirect('home')
    else:
        return render(request, "hello.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully! 'LogOut'")
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = SigUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticated
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Successfully: Register")
            return redirect('home')
        else:
            messages.success(request, "Something error")
            return redirect('register')
    else:
        form = SigUpForm()
        return render(request, "register.html", {'form': form})
