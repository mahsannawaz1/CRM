from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
# Create your views here.


def home(request):
    return render(request, 'user/home.html')


def userRegister(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)
