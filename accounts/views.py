from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import BookInformation

# Create your views here.
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['pass']
        password2=request.POST['re_pass']
        username=request.POST['user_name']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('Username taken.')
                messages.info(request,'username exists')
                print('username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                print('Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print('user created....')
                messages.success(request,'user account created')

                return redirect('login')
        else:
            # print('password not matching ')
            messages.info(request,'password not matched')
            return redirect('register')
        
    # messages.info(request,'account created')
    return render(request,'register.html')

# def register(request):
#     if request.method=='POST':
#         print('post')

#     return render(request,'register.html')
#     # return render(request,'base.html')
    

def login(request):

    if request.method=='POST':
        username=request.POST['your_name']
        passwrod=request.POST['your_pass']
        user=auth.authenticate(username=username,password=passwrod)
        if user is not None:
            auth.login(request,user)
            print('successful login')
            # return redirect('home')
            # return render(request,'content.html',data)
            return redirect('content')
        else:
            print('nope')
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')
    # return redirect('register')

def logout(request):
    auth.logout(request)
    return redirect('home')

def content(request):
    data={
        'books':BookInformation.objects.all()
    }
    return render(request,'content.html',data)

    
def uploadcontent(request):
    if request.method=='POST':
        booktitle=request.POST['book_name']
        author=request.POST['author_name']
        year=request.POST['year']
        genre=request.POST['genre']
        imagefile=request.FILES['upload_file']
        book=BookInformation(title=booktitle,author=author,published_year=year,genre=genre,picture=imagefile)
        book.save()
        messages.info(request,'Book Added!')

        return redirect('content')


    return render(request,'fileupload.html')