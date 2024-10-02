
from django.urls import reverse
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))


    else:
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Користувач успішно створений")
            return HttpResponseRedirect(reverse("users:login"))
        else:
            print("не валідна")
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, "users/register.html", context)

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профіль оновлено")
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        "form": form
    }
    return render(request, "users/profile.html", context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))