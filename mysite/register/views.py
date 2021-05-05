from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(respose):
    if respose.method== "POST":
        form = RegisterForm(respose.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(respose, "register/register.html", {"form":form})
