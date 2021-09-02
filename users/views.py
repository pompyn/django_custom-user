from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import CustomUser
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.conf import settings
from .forms import SignUpForm
"""
for assistance with display of user: https://www.youtube.com/watch?v=jYuGw7o1S0I
"""

# Create your views here.


def index(request):
    user = request.user
    my_user = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'user': user, 'my_user': my_user})


# def account_detail(request, id):
#     user = CustomUser.objects.get(id=id)
#     return render(request, 'account_detail.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    # return request(redirect(''))
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})
