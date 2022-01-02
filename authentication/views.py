from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ADMIN import settings
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        # fname = request.POST['fname']
        # lname = request.POST['lname']
        first_name = request.POST['name']
        # phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Email already exists! Try another email address.")
            return redirect('signup')
        
        # if User.objects.filter(name=first_name):
        #     messages.error(request, "Email already registered!")
        #     return redirect('signup')

        # if len(username)>10:
        #     messages.error(request, "Username must be inder 10 characters")
        #     return redirect('signup')

        if pass1!=pass2:
            messages.error(request, "Password didn't match!")
            return redirect('signup')

        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!")
        #     return redirect('signup')

        myuser = User.objects.create_user(username,first_name,pass1)
        myuser.first_name = first_name
        # myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account Has Been Successfully Created!")


        # Welcome Email

        subject = "Welcome to RefineHealth-Login!"
        message = "Hello "+ myuser.first_name + " !! \nWelcome to refinehealth! \nThank You for visiting our website.\nThanking You,\nTeam refinehealth."
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.username]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('index2')


    return render(request,"authentication/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        logpass = request.POST['logpass']

        user = authenticate(username=username,password=logpass)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "authentication/index2.html", {'fname': fname})
            
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')

    
    return render(request,"authentication/login.html")


def index2(request):
    return render(request, "authentication/index2.html")


def ambulance(request):
    return render(request,"authentication/ambulance.html")


def covid(request):
    return render(request,"authentication/covid.html")


def signout(request):
    logout(request)
    # messages.success(request,"Logged Out Successfully!")
    return redirect('index')