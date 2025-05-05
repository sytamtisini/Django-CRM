from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
 #check to see login
 if request.method== 'POST':
     username=request.POST['username']
     password=request.POST['password']
     
     #Auth
     user =authenticate(request,username=username,password=password)

     if user is not None:
        login(request,user)
        messages.success(request,"You have been logged")
        return redirect('home')
     else:
        messages.success(request,"There was an Error")
        return redirect('home')
     
 else:

     return render(request,'home.html',{})

# login
def login_user(request):
    return render(request,'home.html',{})

# logout
def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out")
    return redirect('home')
# login
def register_user(request):
    return render(request,'register.html',{})
