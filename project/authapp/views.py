from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method=="POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password!=get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is Taken")
                return redirect('/auth/signup')
        except Exception as identifier:
            pass

        myuser= User.objects.create_user (get_email,get_email,get_password)
        myuser.save()
        messages.success(request,'User is created please Login')
        return redirect('/auth/login/')
    return render(request,'signup.html')

def handlelogin(request):
    if request.method=="POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login sucess")
            return redirect('/')
        else:
            messages.error(request,"Invalid credential")
    return render(request,'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request,'Logout success')
    return render(request,'login.html')