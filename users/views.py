from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .register_form import UserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":  # when press signup
        form = UserForm(request.POST)  # all data in form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"welcome {username}")
            return redirect("login")
    else:
        form = UserForm()
    return render(request, "users/register.html", {"form": form})


@login_required()
def profile(request):
    return render(request, "users/profile.html")
