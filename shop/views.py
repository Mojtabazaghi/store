from django.shortcuts import render,HttpResponse,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SingupForm,UpdateUserForm,UpdatePasswordForm

def list(request):
    all_product=Product.objects.all()
    return render (request,'index.html',{'products':all_product})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('login successfully'))
            return redirect ('home')
        else:
            messages.success(request,('not login '))
            return redirect('login')

    return render (request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,('exit'))
    return redirect('home')

def signup_user(request):
    form=SingupForm ()
    if request.method == 'POST':
        form=SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password1)
            login(request,user)
            messages.success(request,'successfully')
            return redirect('home')
        else:
            messages.success(request,'check and try again')
            return redirect('signup')
    else:
        return render(request,'signup.html',{'form':form})
    

def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

def category(request,cat):
    cat=cat.replace('-',' ')
    try:
        category=Category.objects.get(name=cat)
        products=Product.objects.filter(category=category)
        return render (request,'category.html',{'products':products,'category':category})
    except:
        messages.success(request,('category is not found '))
        return redirect('home')



def category_summary(request):
    all_cat=Category.objects.all()
    return render(request,'category_summary.html',{'category':all_cat})


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None,instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request,current_user)
            messages.success(request,'update')
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form})
    else:
        messages.success(request,'please login')
        return redirect('home')


def update_password(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method=='POST':
            form=UpdatePasswordForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'change password successfully')
                login(request,current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('update_password')
        else:
            form=UpdatePasswordForm(current_user)
            return render(request,'update_password.html',{'form':form})
    else:
         messages.success(request,'login')
         return redirect('home')




