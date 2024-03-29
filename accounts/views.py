from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first name']
        last_name=request.POST['last name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name, last_name=last_name)
        if(password1==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user.save()
                print('user created')
                
        else:
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
    
    