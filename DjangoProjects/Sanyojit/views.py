from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm



# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

def login(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, 'login.html',context)

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def home(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "home.html",context)

def contact_us(request):
    title = 'Welcome: This is the Home Page'
    context = {
        "title": title,
    }
    return render(request, "contact_us.html",context)

def list_item(request):
    title = 'List of Items'
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_item.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_item')
    context = {
        "form": form,
        "title": "Add Item",
    }
    return render(request, "add_items.html", context)





