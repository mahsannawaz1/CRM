from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, profileUpdateForm, profileAddressUpdateForm
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


@login_required
def userProfile(request):
    return render(request, 'user/profile.html')


@login_required
def userProfileUpdate(request):

    if request.method == 'POST':
        form_1 = UserUpdateForm(request.POST, instance=request.user)
        form_2 = profileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        form_3 = profileAddressUpdateForm(
            request.POST, instance=request.user.profile.address)
        if form_1.is_valid() and form_2.is_valid() and form_3.is_valid():
            form_1.save()
            form_2.save()
            form_3.save()
            return redirect('profile')
    else:
        form_1 = UserUpdateForm(instance=request.user)
        form_2 = profileUpdateForm(
            instance=request.user.profile)
        form_3 = profileAddressUpdateForm(
            instance=request.user.profile.address)
    context = {
        'form_1': form_1,
        'form_2': form_2,
        'form_3': form_3
    }
    return render(request, 'user/update_profile.html', context)
