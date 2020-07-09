from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login, authenticate, logout
def login_view(request):
    if request.method =="POST":
        form = LoginForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)   
            if user is not None:
                login(request,user)
                return redirect("list")
            return render(request,"account.html",{"form":form})
            
    else:
        form = LoginForm()
        return render(request, "account.html", {"form":form})

def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('sss')
            user=form.save()
            login(request,user)
            return redirect("list")
        return render(request,"account.html",{"form":form})
    else:
        form = RegisterForm()
        return render(request,"account.html",{"form":form})
