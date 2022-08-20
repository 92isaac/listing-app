from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was successfully registered for {username}')
            return redirect('/')
    context ={'forms': form}
    return render(request, 'user/register.html', context)


@login_required
def profile(request):
    updateUser = UserUpdateForm()
    updateProfile = ProfileUpdateForm()
    if request.method == 'POST':
        updateUser = UserUpdateForm(request.POST, instance=request.user)
        updateProfile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if updateUser.is_valid() and updateProfile.is_valid():
            updateUser.save()
            updateProfile.save()

    context={'updateUser': updateUser, 'updateProfile': updateProfile}
    return render(request, 'user/profile.html', context)