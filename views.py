from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login # for login
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is loginpage")

def handlelogin(request):

    if request.method=="POST":
        usname=request.POST.get("name")
        pass1=request.POST.get("password")
        myuser=authenticate(username=usname,password=pass1)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"login success")
            return redirect("index")
        
        else:
            messages.error(request,"Invalid credential")
            return redirect("login")
  
    return render(request,'login.html')


def handlesignup(request):
    if request.method=="POST":
        usname=request.POST.get("name")
        email=request.POST.get("mail")
        passwo=request.POST.get("password")
        confirm=request.POST.get("confirm")
        #print(usname,email,passwo)

        if passwo!=confirm:
            #return HttpResponse("password incorrect")
            messages.warning(request,"password is incorrect")
            return redirect("signup")  
        
        try:
            if User.objects.get(username=usname):
                #return HttpResponse("username is taken")
                 messages.warning(request,"username is taken")
                 return redirect("signup")  
        except:
            pass

        try:
            if User.objects.get(email=email):
                #return HttpResponse("email is taken")
                 messages.warning(request,"email is taken")
                 return redirect("signup")  
            
        except:
            pass

        myuser=User.objects.create_user(usname,email,passwo)
        myuser.save()
        #return HttpResponse("signup successful!!")

        messages.info(request,"signup success please login!!!")
        return redirect("login.html")

    return render(request, 'signup.html')


def about(request):
    return HttpResponse("this is aboutpage")