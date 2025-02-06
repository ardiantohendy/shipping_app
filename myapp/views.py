from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import Cargo
from .forms import CargoForm
# from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credential invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

#user CRUD

@login_required
def check_cargo(request):
    cargos = Cargo.objects.filter(user=request.user)
    return render(request, 'check_cargo.html', {'cargos': cargos})


@login_required
def add_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.user = request.user
            cargo.save()
            return redirect('check_cargo')
    else:
        form = CargoForm()
    return render(request, 'cargo_page.html', {'form': form})


@login_required
def edit_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id, user=request.user)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('check_cargo')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'cargo_form.html', {'form': form})


@login_required
def delete_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id, user=request.user)
    cargo.delete()
    return redirect('check_cargo')

