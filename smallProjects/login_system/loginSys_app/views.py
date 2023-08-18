from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        passConfirm = request.POST.get('cpass')
        if password!=passConfirm:
            return redirect('error')
        else:
            my_user = User.objects.create_user(uname,email,password)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')

def login_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return redirect('error')


    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'user': request.user})



def error(request):
    return render(request, 'failed.html')