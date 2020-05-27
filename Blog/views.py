from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import UserProfile,HomeContents,ImportantLinks,headerimage,NoticeContent,BookShelf,BackToBack2
# Create your views here.
def home(request):
    link=ImportantLinks.objects.all()
    homepost= HomeContents.objects.all()
    back=BackToBack2.objects.all()
    return render(request,'homepage.html',{'link':link, 'homepost':homepost, 'back':back})
def event(request):
    return render(request,'Event.html')

def book(request):
    book=BookShelf.objects.all()
    return render(request,'Book.html',{'book':book})


def notice(request):
    Notice=NoticeContent.objects.all()
    return render(request,'Notice.html',{'NoticeContent':Notice})

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        Password=request.POST['pswd']

        user=auth.authenticate(username=username,password=Password)

        if user is not None:
            auth.login(request,user)
            return redirect('/') 
        else:
            messages.info(request,'InCorrect UserName or Password')
            return redirect('login') 
    else:    
        return render(request,'LogIn.html')

def about(request):

    User=UserProfile.objects.all()

    return render(request,'About.html',{'User':User})


def Segments(request):
    lingk=ImportantLinks.objects.all()
    return render(request,'Segments.html',{'link':lingk})

def myprofile(request):
    return render(request,'userprofile.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method =='POST':
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        Email=request.POST['email']
        Password=request.POST['pswd']
        username=request.POST['username']

        if User.objects.filter(username=username).exists():
            messages.info(request,'User Name Exists')
            return redirect('register')
        elif User.objects.filter(email=Email).exists():
            messages.info(request,'Email Exists')
            return redirect('register')

        user=User.objects.create_user(password=Password,email=Email,first_name=first_name,last_name=last_name,username=username)
        user.save()
        return redirect('login')

    else:
        return render(request,'register.html')

